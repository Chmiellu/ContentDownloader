import os
import smtplib
from email.message import EmailMessage
import ssl

email_sender = 'tomekchmiel2001@gmail.com'
email_password = 'trsu nhsr btys bxbl'
email_receiver = 'tomekchmiel2001@gmail.com'

subject = 'Hope git'
body = """
Śmiga?
"""

context = ssl.create_default_context()

def send_email(file_path):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
            file_name = os.path.basename(file_path)
            em.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    else:
        print(f"The specified file does not exist: {file_path}")
