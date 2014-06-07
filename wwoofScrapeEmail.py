from requests import session
from HTMLParser import HTMLParser
import os
import re
import sys
import codecs



def save_to_txt(text, file_location):
    """Takes a block of html text and saves it to a text file"""
    with codecs.open(file_location, 'w', encoding = 'utf-8') as f:
        f.write(text)

def grab_email(file):
    """Try and grab all emails addresses found within a given file."""
    email_pattern = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b',re.IGNORECASE)
    found = set()
    addresses = []
    if os.path.isfile(file):
        for line in open(file, 'r'):
            found.update(email_pattern.findall(line))
        for email_address in found:
            #print email_address
            addresses.append(email_address)
    return addresses
    #if __name__ == '__main__':grab_email(sys.argv[1])

def gen_list(page,FILE_HTML):
    """calls methods that collect email addresses"""
    save_to_txt(page,FILE_HTML)
    return grab_email(FILE_HTML)



##############################
#  All Together Y'all        #
##############################





def agg_emails(lowerBound, upperBound):
    """
    From lowerBound to upperBound appends the emails from those zones.
    Note that this will not receive from zones under 10, formatted at '05' etc.
    """
        
    URL_LOGIN = 'http://www.wwoof.fr/wwoofers/wmain.php'
    URL_PROTECTED = 'http://www.wwoof.fr/wwoofers/wregion.php?w_region=11'
    FILE_HTML = '~/wwoof.txt'
    FILE_EMAILS = '~/wwoof_emails.txt'
    
    payload = {
        'sublogin' : 'Login',
        'pass': 'XXXXXXX', # Enter password
        'user': 'locke.andrew@gmail.com'
    }
     # Create empty list for addresses 
    all_addresses = []   
    # Clear text file so no doubling of addresses
    open(FILE_EMAILS, 'w').close()
    
    for zone in range(int(lowerBound),int(upperBound)):
        # Cycles through the various zones on WWOOF
        URL_PROTECTED = 'http://www.wwoof.fr/wwoofers/wregion.php?w_region=%s' % (zone,)     
        with session() as c:
            c.post(URL_LOGIN, data=payload)
            request = c.get(URL_PROTECTED)
            #print request.headers
            #print request.text
            page = request.text     
        addresses = gen_list(page,FILE_HTML)
        #print addresses
        #print type(addresses)
        all_addresses += addresses
    
    #print all_addresses
    with open(FILE_EMAILS, 'a') as f:
        f.write(str(all_addresses))
    
    print "Successfully loaded %s addresses" % len(all_addresses)

        
        
def run():
    lowerBound = raw_input('Beginning Zone? --> ')
    upperBound = raw_input('End Zone? --> ')
    agg_emails(lowerBound,upperBound)
        