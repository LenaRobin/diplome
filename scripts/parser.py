from bs4 import BeautifulSoup
import re
import urllib2
import sys

#ouvrir le texte que l'on passe en entree
soup = BeautifulSoup(open("testfile.html"))
    
#for tag in soup.find_all('div class="tags"'):
for search in soup.find_all('div', attrs={'class': re.compile(r"^(url|tags)$")}):
    print search.text.replace(',','').replace('[','').replace(']','').replace('-',' ')



#print sys.argv[1]
