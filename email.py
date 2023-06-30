import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a multipart message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Log in to your email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")

    except Exception as e:
        print("An error occurred while sending the email:", str(e))

    finally:
        # Disconnect from the server
        server.quit()

# Enter your email account details and the email content
sender_email = "dixit.piyush3435@gmail.com"
sender_password = "Piyush@123"
recipient_email = "@example.com"
subject = "Hello!"
message = "This is a test email."

# Send the email
send_email(sender_email, sender_password, recipient_email, subject, message)