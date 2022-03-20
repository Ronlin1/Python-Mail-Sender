import smtplib
from email.message import EmailMessage

def send_email(send_email_to):
      msg = EmailMessage()
      
      msg['From'] = "sender@gmail.com"
      msg['To'] = send_email_to
      msg['Subject'] = "Sending Emails With Python!"
      message = msg.set_content("We are using Python >>")

      # Send the message via our own SMTP server.
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.login("yourmail@gmail.com", "yourpassword")
      server.send_message(msg)
      server.quit()

      # prints to your console
      print("Successfully sent email to %s:" % (msg['To']))
      
send_email("recipientmail@gmail.com")