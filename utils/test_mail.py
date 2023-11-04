import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from django.http import HttpResponse

def send_email(subject, message, sender_email, recipient_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a MIME object
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # Attach text message
    msg.attach(MIMEText(message, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use TLS for secure connection
            server.login(smtp_username, smtp_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, msg.as_string())

            return HttpResponse("Email sent successfully!")

    except smtplib.SMTPException as e:
        print("inside smtplib error",e)
        return HttpResponse(f"Email could not be sent. Error: {str(e)}")
        
    except Exception as e:
        print("eception",e)

        return HttpResponse(f"An error occurred: {str(e)}")
