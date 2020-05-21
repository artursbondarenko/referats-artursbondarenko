from bs4 import BeautifulSoup
from urllib.request import *
 
url = 'https://wallhaven.cc/search?q=id%3A537&sorting=random&ref=fp&seed=MIxrC&page=1'

def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html
 
def main():
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    for i in range(1):
        html = get_html(url +str(i))
        soup = BeautifulSoup(html, 'html.parser')
        saraksts = soup.find_all(class_='preview')
        for a in saraksts:
            secondary_html = get_html(a['href'])
            secondary_soup = BeautifulSoup(secondary_html, 'html.parser')
            bilde = secondary_soup.find(id='wallpaper')['src']
            urlretrieve(bilde, "bilde.jpg"  )
            print('Download')
 
main()
