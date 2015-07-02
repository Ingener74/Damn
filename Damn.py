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
    get = 'http://damn.ru/?' + urllib.urlencode({
        'name': name,
        'sex': 'm' if sex else 'w'
    })

    response = urllib2.urlopen(get)

    soup = BeautifulSoup.BeautifulSoup(response.read())

    return soup.findAll('div', {'class': 'damn'})[0].text.replace('&mdash;', '')

print getDamn('Паша')
