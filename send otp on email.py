#python 3.7.1
import random
import smtplib
def Otp_mail():
    OTP=random.randint(100000,999999)
    return OTP 
email=input("Enter your email..:")
obj=Otp_mail()
smtp_server="smtp.gmail.com"
smtp_port=587
smtp_username="noorani.manuu@gmail.com"
password="urpz knts emsc wijj"
server=smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(smtp_username, password )
Msg="Your OTP "
subject=f"your otp is,:{obj} please don't share your otp"
from_email=f"email"
server.sendmail(from_email,email,f"Msg:{Msg}\n\n{subject}")
