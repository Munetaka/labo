import requests
from bs4 import BeautifulSoup as soup


def get_links(url):
    result = requests.get(url)
    # page = result.page # get error no page object
    page = result.text
    # doc = soup(page) # get result & error
    doc = soup(page, 'lxml')
    links = [element.get('href') for element in doc.find_all('a')]
    return links


if __name__ == '__main__':
    import sys
    for url in sys.argv[1:]:
        print('Links in', url)
        for num, link in enumerate(get_links(url), start = 1):
            print(num, link)
        print()
