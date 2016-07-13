import smtplib
import sys

def send_email(user, pwd, recipient, subject, body, dm):

    # gmail_user = user
    # gmail_pwd = pwd
    # FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (user, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP(dm, 587) #("smtp.gmail.com", 587)#('smtp.googlemail.com', 465)#
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, TO, message)
        server.close()
        print 'successfully sent the mail'
    except Exception as e:
        if (dm.__contains__("gmail") or dm.__contains__("google")):
            print "Unable to send message", "You may need to go to https://www.google.com/settings/security/lesssecureapps and set your account to work with less secure apps. Actual error follows: " + str(e)
        else:
            print "Unable to send message", str(e)

stop = raw_input("This email program was designed with gmail smpt in mind but it may work with other domain accounts.\nTo use it you will need your username (e-mail) and password.\nYou may also need to go to https://www.google.com/settings/security/lesssecureapps and set your account to work with less secure apps. Do you wish to continue (y/n)? ").lower().strip()

while (stop!="y" and stop!="n"):
    stop = raw_input("This email program was designed with gmail smpt in mind but it may work with other domain accounts.\nTo use it you will need your username (e-mail) and password.\nYou may also need to go to https://www.google.com/settings/security/lesssecureapps and set your account to work with less secure apps. Do you wish to continue (y/n)? ").lower().strip()

if (stop=="n"):
    exit()

domain=raw_input("Please enter a domain name, if left blank smtp.gmail.com will be used: ").lower().strip()

if (domain.__len__()==0):
    domain = "smtp.gmail.com"

user=raw_input("Please enter your user or email address or enter 'c' to cancel. If left blank a default email address will be used: ").lower().strip()

if (user.__len__()==0):
    user = "cristianbyfaith@gmail.com"

if (user=="c"):
    exit()

password=raw_input("Please enter your password or enter 'c' to cancel, if left blank a default password will be used: ").strip()

if (password.__len__()==0):
    password = "thinkpad1"

if (password=="c"):
    exit()

target=raw_input("Please enter target email address or c to cancel, if left blank a default email address will be used: ").lower().strip()

if (target.__len__()==0):
    target = "cristianbyfaith@gmail.com"

if (target=="c"):
    exit()

e_subject=raw_input("Please enter the subject of the message or enter c to cancel, if left blank subject will be 'test': ").strip()

if (e_subject.__len__()==0):
    e_subject = "test"

if (e_subject=="c" or e_subject == "C"):
    exit()

e_body = raw_input("Please enter the body of the message or enter c to cancel, if left blank the body will be 'test': ").strip()

while (e_body.__len__() == 0):
    e_body = "test"

if (e_body == "c" or e_body == "C"):
    exit()

send_email(user,password,target, e_subject,e_body,domain)

