# Here I will try to learn how to make Web Scrapping

# import libraries
import datetime
import json
import requests
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://www.fidelcastro.cu/es/discursos/palabras-de-fidel-castro-ruz-momentos-antes-de-partir-hacia-el' \
             '-cuartel-moncada-26-julio '

# query the website and return the html to the variable ‘page’
page = requests.get(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.content, 'html.parser')

# finding the title of the speech
title_box = soup.find('h1', attrs={'class': 'node-title'})
title = title_box.text.strip()

# Here I recover the text of the speech and more stuff
speech = []
for blabla in soup.find_all('div', attrs={'class': 'field-item even'}):
    speech.append(blabla.text.strip())
print(speech)

# To recover the date
date = speech[0]
text = speech[1]

# Here I create a Python dictionary to store the information from the speech
discourse = {'Date': date, 'Title': title, 'Text': text}

with open('index.json', 'w') as ID:
    json.dump(discourse, ID)

# finding the date of the speech
# date_box = soup.find('span', attrs={'class': 'date-display-single'})

# date = date_box.text.strip()  # strip() is used to remove starting and trailing
# date_d = datetime.datetime.strptime(date, '%d/%m/%Y').date()
