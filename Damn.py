#encoding: utf8

import urllib
import urllib2

from bs4 import BeautifulSoup

def getDamn(name, sex=0):
	"""
	name - Имя
	sex  - 0 для мужика, 1 - для бабы
	"""
	SITE = 'http://damn.ru/'
	
	query = {
		'name':name,
		'sex': 'm' if sex == MEN else 'w'
		}
	
	get = SITE + '?' + urllib.urlencode(query)
	
	response = urllib2.urlopen(get)

	soup = BeautifulSoup(response.read())
	
	return soup.find_all('div', {'class':'damn'})[0].text

print getDamn('Паша')