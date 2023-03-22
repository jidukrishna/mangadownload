from bs4 import BeautifulSoup
import requests
def chapl(url):
    chaplist=[]
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'lxml')
    b=soup.find_all('li',class_='a-h')
    b=str(b).split()
    for i in b:
        if i.startswith('href='):
            op=i.lstrip('href=').rstrip('>').strip('''"''')
            chaplist.append(op)
    chapterlist=chaplist[::-1]
    return chapterlist

if __name__=='__main__':
    print(chapl('https://chapmanganato.com/manga-jn986670'))