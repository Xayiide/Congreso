#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs


urls = []
base_url = "https://www.congreso.es/cem/"

# sub_urls = [periodo.get('href') for periodo in bs(requests.get(base_url + 'xivleg').text, 'html.parser').findAll('a', {'class':'titleorimageid1siteid73 point-list'})]

req  = requests.get(base_url + 'xivleg')
sopa = bs(req.text, 'html.parser')
periodos = sopa.findAll('a', {'class':'titleorimageid1siteid73 point-list'})

for periodo in periodos:
    urls.append(periodo.get('href'))

paginas_periodos = []

for url in urls:
    paginas_periodos.append(requests.get(base_url + url))

elegida = paginas_periodos[4]
sopa    = bs(elegida.text, 'html.parser')

