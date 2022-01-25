import time
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMessage

from_mail = settings.FROM_EMAIL


def send_email(from_email, to, subject, message, html=True):
    """
    Send emails to the given recipients
    :param from_email:
    :param to:
    :param subject:
    :param message:
    :param html:
    :return: Boolean value
    """
    try:
        email = EmailMessage(subject, message, from_email, to)
        print("Sending email..")
        if html:
            email.content_subtype = 'html'
        email.send()
        return True
    except Exception as e:
        print("Error in sending email: {0}".format(str(e)))
        if 'rate exceeded' in str(e):
            time.sleep(2)
            send_email(from_email, to, subject, message)

        return False


# Function for sending trigger mails to the Admin when Server error occurs
def book_alert_mail(user_email):
    """
        Function to send Test mails due to Server Error
    """
    print("Sending the Test Mail for testing")

    subject = "Book Action Mail - <Date>"
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    subject = subject.replace("<Date>", str(dt_string))
    email_template = """
    Hi,
    
    The user have borrowed/returned the book
    """
    send_email_response = send_email(from_mail, user_email, subject, email_template, html=True)
    if send_email_response is True:
        print("Mail successfully sent")
    else:
        print("Mail not sent")
