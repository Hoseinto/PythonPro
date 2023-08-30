import requests
import re
from bs4 import BeautifulSoup
r = requests.get ('https://divar.ir/s/tehran')
soup = BeautifulSoup (r.text,'html.parser')
val = soup.find_all ('article')
for i in range (0,len (val)):
    if 'توافقی' in val[i].text:
        print (val[i].text)
