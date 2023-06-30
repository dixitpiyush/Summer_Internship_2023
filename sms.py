from twilio.rest import Client

def send_sms(account_sid, auth_token, sender_phone_number, recipient_phone_number, message):
    try:
        # Create a Twilio client
        client = Client(account_sid, auth_token)

        # Send the message
        client.messages.create(
            body=message,
            from_=sender_phone_number,
            to=recipient_phone_number
        )
        print("SMS sent successfully!")

    except Exception as e:
        print("An error occurred while sending the SMS:", str(e))

# Enter your Twilio account SID, auth token, phone numbers, and the message content
account_sid = "your_account_sid"
auth_token = "your_auth_token"
sender_phone_number = "+9178*******35"  # Your Twilio phone number
recipient_phone_number = "+9170*******61"  # Recipient's phone number
message = "Hello, bro"

# Send the SMS
send_sms(account_sid, auth_token, sender_phone_number, recipient_phone_number, message)
