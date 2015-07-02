# encoding: utf8

import urllib
import urllib2

# noinspection PyUnresolvedReferences
import BeautifulSoup

# noinspection PyPep8Naming
def getDamn(name, sex=1):
    """
    name - Имя
    sex  - 1 для мужика, 0 - для бабы
    """
    SITE = 'http://damn.ru/'

    query = {
        'name': name,
        'sex': 'm' if sex else 'w'
    }

    get = SITE + '?' + urllib.urlencode(query)

    response = urllib2.urlopen(get)

    soup = BeautifulSoup.BeautifulSoup(response.read())

    out = soup.findAll('div', {'class': 'damn'})[0].text

    return out.replace('&mdash;', '')

print getDamn('Паша')
