import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


def extract_words(soup: BeautifulSoup):
    words = []
    divs = soup('div')
    for div in divs:
        div_class = div.get('class', None)
        if div_class:
            continue
        if div_class[0] == 'glface':
            words.append(div.contents[0])
    return words


def extract_links(soup: BeautifulSoup):
    links = soup('a')
    return [link.get('href', None) for link in links if link.get('href', "").startswith('/ielts-list')]


def extract_data(url=None):
    base_url = 'https://www.examword.com'

    if url is None:
        url = '/ielts-list/4000-academic-word-1?la=ru'

    full_url = base_url + url

    html = urllib.request.urlopen(full_url).read()
    return BeautifulSoup(html, 'html.parser')
