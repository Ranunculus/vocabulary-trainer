import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

base_url = 'https://www.examword.com'


def extract_words(soup: BeautifulSoup):
    words = []
    divs = soup('div')
    for div in divs:
        div_class = div.get('class', None)
        if div_class is None: continue
        if div_class[0] == 'glface':
            words.append(div.contents[0])
    return words


def extract_links(soup: BeautifulSoup):
    links_to_continue = []
    links = soup('a')
    for link in links:
        href = link.get('href', None)
        if href.startswith('/ielts-list'):
            links_to_continue.append(href)
    return links_to_continue


def extract_data(url=None):
    if url is None: url = '/ielts-list/4000-academic-word-1?la=ru'
    full_url = base_url + url

    x = urllib.request.urlopen(full_url)
    html = x.read()
    return BeautifulSoup(html, 'html.parser')
