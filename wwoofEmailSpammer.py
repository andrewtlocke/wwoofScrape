# -*- coding: utf-8 -*-
import smtplib 
import random

FILE_EMAILS = '~/wwoof_emails.txt'
FILE_SENT_EMAILS = '~/wwoof_sent_emails.txt'

# Load email address
with open(FILE_EMAILS,'r') as f:
    all_emails = f.read().splitlines()
#for i in all_emails: print i
f.close()

num_emails = len(all_emails)

# Generate random numbers 
randoms = []
num_desired = 60
check = 1


while check <= num_desired:
    random.seed(check)
    randoms.append(random.randrange(1,num_emails,1))
    check += 1

# Get smaller subset of all_emails using randoms list
to_email = []
for random in randoms:
    to_email.append(all_emails[random])
     

## HERE we go.

#recipients = to_email
#recipients = ['locke.andrew@gmail.com']

for recipient in recipients:
    fromaddr = 'locke.andrew@gmail.com'
    toaddrs = recipient
    msg = "\r\n".join([
    "From: locke.andrew@gmail.com",
    "To: recipient",
    "Subject: Travailler sur ton ferme",
    "",
    ( "Bonjour! \n \n" 
    "Je m'appelle Andrew et j'habite á Boston. "
    "En trois semaines je viendrai en France. " 
    "Je pense que votre ferme est magnifique, " 
    "et, si possible, je voudrais venir travailler avec vous pendant deux semaines "
    "- du 30 avril au 15 mai. \n \n"
    "Quand j'étais un petit garçon, j'ai travaillé sur une ferme avec ma famille. " 
    "Et avec WWOOF, j'ai travaillé en Jordanie et Egypte. " 
    "Je peux travailler avec du bois et des animaux. " 
    "Je suis un bon travailleur et je peux apprendre rapidement. \n \n "
    "J'apprends le français et je veux parler et pratiquer. " 
    "Je peux enseigner l'anglais ou l'espagnol ou l'arabe; "
    "á Boston, je suis économiste et je suis en mesure d'aider avec les ordinateurs, si vous voulez. "
    "Aussi, je sais céramique. \n \n"
    "Mon numéro de membre WWOOF est FR 76082.\n \n"
    "Si vous avez des questions, n'hésitez pas a me contacter! \n \n"
    "Merci beaucoup! \n \n"
    "Andrew")
    ])
    
    # Credentials
    username = 'locke.andrew@gmail.com'
    password = 'XXXXXXXX' # Enter pw
    
    # The mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit

# Save to sent text file
with open(FILE_SENT_EMAILS, 'a') as f:
    for email in recipients:
        f.write("%s\n" % email)

