import getpass

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    # try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print 'successfully sent the mail'
    # except:
    #     print "failed to send mail"

gmail_addr = raw_input("Email account to send from: ")
password = getpass.getpass("Enter your password (will not be stored): ")

send_email(gmail_addr,password,"cs1160396@iitd.ac.in","ABC","XYZ")