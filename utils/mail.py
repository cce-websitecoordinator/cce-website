

from dotenv import load_dotenv

import base64
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
import random,math,os



load_dotenv()
project_id = os.getenv("PROJECT_ID")
private_key_id = os.getenv("PRIVATE_KEY_ID")
private_key = os.getenv("PRIVATE_KEY")
client_id = os.getenv("CLIENT_ID")


jsonk = {
    "type": "service_account",
    "project_id": project_id,
    "private_key_id": private_key_id,
    "private_key": private_key,
    "client_email": "grievance@grievance-377905.iam.gserviceaccount.com",
    "client_id": client_id,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/grievance%40grievance-377905.iam.gserviceaccount.com",
}


credentials = service_account.Credentials.from_service_account_info(
    jsonk,
    scopes = ['https://mail.google.com/'],
    subject='grievance@cce.edu.in'
)

service = build('gmail', 'v1', credentials=credentials)

def msg_send(recepients,name,email,message_data):
    """
    Sends a message containing grievance confirmation to the specified recipients.

    Args:
        recepients (str): A comma-separated string containing the email addresses of the recipients.
        name (str): The name of the sender.
        email (str): The email address of the sender.
        message_data (str): The message to be sent.

    Returns:
        dict: A dictionary containing the response received after sending the message.
    """
    subject = "Grievance confirmation"
    with open('templates/utils/mail.html','r') as file:
        data = file.read()
    data = data.replace("_namedata_",name)
    data = data.replace("_datedata_",str(date.today()))
    data = data.replace("_emaildata_",email)
    data = data.replace("_messagedata_",message_data)
    message = MIMEMultipart()
    message.attach(MIMEText(data, "html"))

    message['To'] = recepients
    message['From'] = 'grievance@cce.edu.in'
    message['Subject'] = subject

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {
            'raw': encoded_message
        }

    send_message = (service.users().messages().send(userId="me", body=create_message).execute())
    return send_message

def create_otp():
    digits = "0123456789"
    otp = ""

    for i in range(4) :
        otp += digits[math.floor(random.random()*10)]
    
    return otp

def send_otp(recepients, otp):
    """
    The function `send_otp` sends an email containing an OTP (One-Time Password) to the specified
    recipients.
    
    :param recepients: The `recepients` parameter is a string that represents the email address of the
    recipient(s) to whom the OTP (One-Time Password) will be sent. It can be a single email address or
    multiple email addresses separated by commas
    :param otp: The `otp` parameter is the One-Time Password that will be sent to the recipients for
    verification
    :return: The function `send_otp` returns the result of the `send_message` method call, which is the
    response from the Gmail API after sending the email message.
    """
    subject = "OTP for verification"
    with open('code.html', 'r') as file:
        data = file.read()

    data = data.replace("_otpdata_", otp)
    message = MIMEMultipart()
    message.attach(MIMEText(data, "html"))

    message['To'] = recepients
    message['From'] = 'grievance@cce.edu.in'
    message['Subject'] = subject

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {
        'raw': encoded_message
    }

    send_message = service.users().messages().send(userId="me", body=create_message).execute()
    return send_message


def main():
    import os
    print("Current working directory:", os.getcwd())
    recepients = 'amalmanoj02@gmail.com,sai.prasad.1603@gmail.com'
    name = "Sai"
    email = "grievance@cce.edu.in"
    message = "Grievance is grievance and the good things"

    message_sent = msg_send(recepients,name,email,message)

    print(message_sent)

    # otp = create_otp()

    # otp_Sent = send_otp(recepients,otp)

    # print(otp_Sent)

main()