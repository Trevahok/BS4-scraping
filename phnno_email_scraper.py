from bs4 import BeautifulSoup
import re
from urllib.request import urlopen,Request

webp=input('enter the webpage name:')
req = Request(webp, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

f = urlopen(req).read()

s = BeautifulSoup(f, 'html.parser')
s = s.get_text()
plusphone=re.findall(r'\+[0-9\-\s]{6,}',s)
phone = re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",s)
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",s)
phone+=plusphone
if len(phone) == 0:
    print ("Sorry, no phone number found.")

    print('------------')
else :
    count = 1
    for item in phone:
        print ( count, ' phone number(s) found : ',item )
        count += 1

print('------------')

if len(emails) == 0:
    print("Sorry, no email address found.")
    print('------------')
else:
    count = 1
    for item in emails:
        print(count, ' email address(es) found : ', item)
        count += 1
