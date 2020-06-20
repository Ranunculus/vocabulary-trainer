import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def extract_words(soup: BeautifulSoup):
    words = []
    divs = soup('div')
    for div in divs:
        div_class = div.get('class', None)
        if (div_class is None):
            continue
        if (div_class[0] == 'glface'):
            words.append(div.contents[0])
    return words

def extract_links(soup: BeautifulSoup):
    links_to_continue = []
    links = soup('a')
    for link in links:
        href = link.get('href', None)
        if ( href.startswith('/ielts-list') ):
            links_to_continue.append(href)
    return links_to_continue

if __name__ == "__main__":
    base_url = 'https://www.examword.com'
    url = base_url + '/ielts-list/4000-academic-word-1?la=ru'

    x = urllib.request.urlopen(url)
    html = x.read()
    soup = BeautifulSoup(html, 'html.parser')





