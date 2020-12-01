import smtplib
import time #sleep
from string import Template
from I_Voted.election.url_service.uuid_engine import new_id

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'smitvotes.noreply@gmail.com'
PASSWORD = '$thisisabot#'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.title().split('_')[0])
            emails.append(a_contact)
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def send_mails():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    # s.set_debuglevel(1)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        url_id = new_id(email)
        if url_id == None:
            continue
        message = message_template.substitute(PERSON_NAME=name.title(), request_id=url_id)

        # Prints out the message body for our sake
        print("sending mail to : ",email,'\n')

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        time.sleep(2)
        
    # Terminate the SMTP session and close the connection
    s.quit()
