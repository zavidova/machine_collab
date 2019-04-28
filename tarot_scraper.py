import urllib2
from bs4 import BeautifulSoup
import sys
import requests
import pprint
import re
import pyperclip


reload(sys)
sys.setdefaultencoding('utf8')


#all the individual artists' profile pages go there

urls = [

'https://supertarot.co.uk/knight-of-disks/',
'https://supertarot.co.uk/prince-of-wands/',
'https://supertarot.co.uk/aeon/',
'https://supertarot.co.uk/four-luxury/',
'https://supertarot.co.uk/three-work/',
'https://supertarot.co.uk/two-love/',
'https://supertarot.co.uk/two-peace/',
'https://supertarot.co.uk/nine-strength/',
'https://supertarot.co.uk/prince-of-swords/',



]


for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    content_box = soup.find('div', attrs={'class':'content-area'})
    content = content_box.text.strip()
    print (content)
