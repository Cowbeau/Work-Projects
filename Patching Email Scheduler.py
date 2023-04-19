import smtplib
import schedule
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set email parameters
to_email = 'recipient@example.com'
from_email = 'sender@example.com'
subject = 'Email subject goes here'
body = 'This is the email body.'

# Define function to send email
def send_email():
    # Create message object
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Send email using SMTP server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(from_email, 'your-password-here')
    smtp_server.sendmail(from_email, to_email, message.as_string())
    smtp_server.quit()

# Define function to schedule email sending
def schedule_email():
    # Get today's date
    today = datetime.datetime.today()

    # Get the date of the third Tuesday of the month
    third_tuesday = today.replace(day=15, hour=8, minute=30)
    while third_tuesday.weekday() != 1:
        third_tuesday += datetime.timedelta(days=1)
    if third_tuesday < today:
        third_tuesday = (today.replace(day=15) + datetime.timedelta(days=31)).replace(hour=8, minute=30)

    # Schedule email sending
    schedule.every().month.at(third_tuesday.strftime('%H:%M')).do(send_email)

# Schedule email sending
schedule_email()

# Run the scheduled tasks
while True:
    schedule.run_pending()

