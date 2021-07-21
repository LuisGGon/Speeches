# Here I will try to learn how to make Web Scrapping

# import libraries
import json
import requests
from bs4 import BeautifulSoup

# Here I create the list of the pages where speeches are.
# There 150 pages with Fifo's speeches.

pages = ['http://www.fidelcastro.cu/es/discurso']  # This is the "zero" page

for k in range(1, 151):
    pages.append('http://www.fidelcastro.cu/es/discurso?page=' + str(k))


def links_by_page(url):
    # This function receives the url with the links to Fifo's speeches and collect those links.

    web = requests.get(url)
    web_soup = BeautifulSoup(web.content, 'html.parser')

    # Here we collect all the links in one web page
    # Idea from https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/

    all_links = []
    links = web_soup.select('a')

    for ahref in links:
        txt = ahref.text
        txt = txt.strip() if txt is not None else ''

        href = ahref.get('href')
        href = href.strip() if href is not None else ''
        all_links.append({"href": href, "text": txt})

    # Now I want to filter the links that comes with 'ver más'
    # Idea from https://www.delftstack.com/howto/python/python-search-list-of-dictionaries/

    real_links = [x for x in all_links if x['text'] == 'ver más']
    return real_links


# specify the url
quote_page = 'http://www.fidelcastro.cu/es/discursos/palabras-de-fidel-castro-ruz-momentos-antes-de-partir-hacia-el' \
             '-cuartel-moncada-26-julio '


def scrape_fifo(url):
    # This function receives an url with a Fifo's speech and extracts its date, title and content.

    page = requests.get(quote_page)  # query the website and return the html to the variable 'page'
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page.content, 'html.parser')

    # finding the title of the speech
    title_box = soup.find('h1', attrs={'class': 'node-title'})
    title = title_box.text.strip()

    # Here I recover the text of the speech and more stuff
    speech = []
    for blabla in soup.find_all('div', attrs={'class': 'field-item even'}):
        speech.append(blabla.text.strip())

    # To recover the date and content of the speech
    date = speech[0]
    text = speech[1]
    text = text.split('\n')

    # Here I create a Python dictionary to store the information from the speech
    discourse = {'Date': date, 'Title': title, 'Text': text}

    with open('index.json', 'w') as ID:
        json.dump(discourse, ID)

    return


def speeches_link():
    # This function creates a list with the links to all Fifo's speeches.

    links = []
    for j in pages:
        temp = links_by_page(j)
        for i in temp:
            links.append(i['href'])

    return links


print(links_by_page(pages[10]))


print(len(speeches_link()))

scrape_fifo(quote_page)
