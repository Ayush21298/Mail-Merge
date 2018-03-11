# Python code to illustrate Sending mail from 
# your Gmail account 
import getpass
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
s.ehlo();
# start TLS for security
s.starttls()
 
# Authentication
gmail_addr = raw_input("Email account to send from: ")
password = getpass.getpass("Enter your password (will not be stored): ")
s.login(gmail_addr, password)
 
# message to be sent
message = "Message_you_need_to_send"
 
# sending the mail
s.sendmail(gmail, "cs1160396@iitd.ac.in", message)
 
# terminating the session
s.quit()