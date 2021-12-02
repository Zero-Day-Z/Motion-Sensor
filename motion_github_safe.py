from gpiozero import LED
from gpiozero import MotionSensor
import time
import smtplib
from datetime import datetime

##Sending the email
#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = #ENTER THE EMAIL YOU WANT TO SEND THE NOTIFICATION FROM HERE. EXAMPLE: 'someone@gmail.com'
GMAIL_PASSWORD = #ENTER THE PASSWORD OF THE ABOVE EMAIL ADDRESS HERE. EXAMPLE: '543210'

class Emailer:
    def sendmail(self, recipient,  subject, content):
        #Creating the headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, 
            "To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
green_led = LED(17)
pir = MotionSensor(4)
green_led.off()

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    green_led.on()
    pir.wait_for_no_motion()
    
    sender = Emailer()
    sendTo =  #ENTER RECIEVEING EMAIL ADDRESS HERE IN SINGLE QUOTES. EXAMPLE:'someone@gmail.com'
    emailSubject = #ETNER EMAIL SUBJECT HERE. EXAMPLE: "IOT Research: Motion In the lab "
    emailContent = # ENTER EMAIL CONTENTS HERE. EXAMPLE: "This is the Pi in the lab.\n Someone has entered our lair!"

    #Sends an email to the "snedTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
    sender.sendmail(sendTo, emailSubject, emailContent)
    
    if pir.wait_for_no_motion() :
        green_led.off()
        print("Motion Stopped")
    
    
