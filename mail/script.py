import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import os
import datetime

# Email credentials
EMAIL_ADDRESS = 'firfirfas@gmail.com'
EMAIL_PASSWORD = 'xicg xyru vpzd benm'

# Recipients
TO_EMAIL = 'uktentu@outlook.com'
SUBJECT = 'Daily Report for testing'

def create_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    return msg

def send_email(msg):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, msg['To'], msg.as_string())
        print('Email sent successfully.')
    except Exception as e:
        print(f'Failed to send email. Error: {e}')

def attach_file(msg, file_path):
    try:
        with open(file_path, 'rb') as file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
            msg.attach(part)
    except Exception as e:
        print(f'Failed to attach file. Error: {e}')

def main():
    # Generate the email content
    today = datetime.date.today().strftime("%Y-%m-%d")
    body = f"Please find the attached daily report for {today}."
    msg = create_email(SUBJECT, body, TO_EMAIL)

    # Attach a report file (if any)
    report_file_path = 'mail/report/report.txt'
    if os.path.exists(report_file_path):
        attach_file(msg, report_file_path)
    else:
        print(f'Report file not found: {report_file_path}')

    # Send the email
    send_email(msg)

if __name__ == '__main__':
    main()
