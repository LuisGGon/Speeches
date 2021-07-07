# Here I will try to learn how to make Web Scrapping

# import libraries

import requests
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://www.fidelcastro.cu/es/discursos/palabras-de-fidel-castro-ruz-momentos-antes-de-partir-hacia-el' \
             '-cuartel-moncada-26-julio '

# query the website and return the html to the variable ‘page’
page = requests.get(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.content, 'html.parser')