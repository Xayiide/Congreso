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

print(urls)

for url in urls:
    paginas_periodos.append(requests.get(base_url + url))

for pagina in paginas_periodos:
    sopa = bs(pagina.text, 'html.parser')
    tabla = sopa.find('table', {'class':'t_no_border'})
    print(pagina.url)
    tbody = tabla.find('tbody')
    filas = tbody.findAll('tr')
    for fila in filas:
        print(dir(fila))


