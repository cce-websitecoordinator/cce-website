import os
import boto3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from django.http import HttpResponse
from botocore.exceptions import ClientError
from django.http import HttpResponse

def send_email(subject, message, recipient_email,template_values=None):
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    # Create a new SES resource
    ses = boto3.client('ses', region_name='ap-south-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,)

    # Try to send the email
    # Create a MIME object
    msg = MIMEMultipart()
    msg["From"] = "Grievance Cell - CCE <grivance@cce.edu.in>"
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # Attach text message
    msg.attach(MIMEText(message, "plain"))
    path = os.getcwd()
    html_template = path + '/utils/mail.html'

    # Attach HTML template if provided
    if html_template:
        # Load HTML template and replace placeholders
        with open(html_template, "r") as file:
            html_content = file.read()

        if template_values:
            for key, value in template_values.items():
                html_content = html_content.replace(f"{{{{{key}}}}}", str(value))

        msg.attach(MIMEText(html_content, "html"))

    # Try to send the email
    try:
        # Provide the contents of the email
        response = ses.send_raw_email(
            Source='grivance@cce.edu.in',
            Destinations=[recipient_email],
            RawMessage={'Data': msg.as_string()}
        )

        return HttpResponse(f"Email sent successfully! Message ID: {response['MessageId']}")

    except ClientError as e:
        print("AWS SES error:", e.response['Error']['Message'])
        return HttpResponse(f"Email could not be sent. Error: {e.response['Error']['Message']}")

    except Exception as e:
        print("Exception:", e)
        return HttpResponse(f"An error occurred: {str(e)}")
