# testing out whether i can actually define and call a function in python

from BeautifulSoup import BeautifulSoup
import re
import urllib2


#a = "http://www.kechg.org"
#b = input('Type another word:')

	
url = urllib2.urlopen("http://www.kngs.co.uk")
content = url.read()
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True):
	if re.findall('python', a['href']):
		print "Found the URL:", a['href']
	#print(soup)


#dosomething()

#def addstuff(a,b):
#	c = a + b
#	return c


#print(addstuff(a,b))
