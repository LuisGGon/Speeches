# Here I will try to learn how to make Web Scrapping

# import libraries
import datetime
import requests
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://www.fidelcastro.cu/es/discursos/palabras-de-fidel-castro-ruz-momentos-antes-de-partir-hacia-el' \
             '-cuartel-moncada-26-julio '

# query the website and return the html to the variable ‘page’
page = requests.get(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.content, 'html.parser')

# finding the date of the speech
date_box = soup.find('span', attrs={'class': 'date-display-single'})

date = date_box.text.strip()  # strip() is used to remove starting and trailing
date_d = datetime.datetime.strptime(date, '%d/%m/%Y').date()

# finding the title of the speech
title_box = soup.find('h1', attrs={'class': 'node-title'})

title = title_box.text.strip()
print(title)

discourse = {'Date': date, 'Title': title}
print(discourse)
