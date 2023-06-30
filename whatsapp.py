import pywhatkit

#sender's phone number
phone_number = "+9170******761" 

#message what you want to send
message = "This is Adi!"


pywhatkit.sendwhatmsg_instantly(phone_number, message)
print("WhatsApp message sent!")