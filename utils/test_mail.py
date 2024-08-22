import os
import boto3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from django.http import HttpResponse
from botocore.exceptions import ClientError
from django.http import HttpResponse

def send_email(subject, message, recipient_email, template_values=None):
    try:
        aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
        # Create a new SES resource
        ses = boto3.client('ses', region_name='ap-south-1', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,)

        # Create a MIME object
        msg = MIMEMultipart()
        msg["From"] = "Grievance Cell - CCE <grivance@cce.edu.in>"
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Attach text message
        # msg.attach(MIMEText(message, "plain"))
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
        response = ses.send_raw_email(
            Source='grivance@cce.edu.in',
            Destinations=[recipient_email,"grievance@cce.edu.in"],
            RawMessage={'Data': msg.as_string()}
        )

        return response, None  # Return response and no error

    except ClientError as e:
        error_message = f"AWS SES error: {e.response['Error']['Message']}"
        return None, error_message

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return None, error_message


