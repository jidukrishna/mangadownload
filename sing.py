from bs4 import BeautifulSoup
import requests
def sim(url):
    headers = {
        'referer': f'Referer: {url}'
    }
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, 'lxml')

    a = soup.find_all('div', 'container-chapter-reader')
    b = str(a).split()
    imgl = []
    for i in b:
        if i.startswith('src=') and i.endswith('.jpg"'):
            c = i.lstrip('src=').strip('"')
            imgl.append(c)


    return imgl


if __name__=='__main__':
    sim('https://chapmanganato.com/manga-ph966790/chapter-15.2')