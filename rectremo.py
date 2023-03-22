import requests
from bs4 import BeautifulSoup
def trending():
    url = 'https://mangareader.to/home'
    r = requests.get(url).content
    soup = BeautifulSoup(r, 'lxml')
    a = soup.find_all('div', class_='anime-name')
    c = 0
    print('''
    ----------------------Trending----------------------''')
    for i in a:
        c += 1
        print(f'{c}.{i.text}')
def mv(no):
    tup=('today','week','month')
    mv=tup[no]
    url = 'https://mangareader.to/home'
    r = requests.get(url).content
    soup = BeautifulSoup(r, 'lxml')
    a = soup.find_all('div', {'id': f'chart-{mv}'})[0]
    a = str(a).split(',')
    c = 0
    print(f'''
    ----------------------Most viewed {mv}----------------------''')
    for i in a:
        if 'title=' in i:
            c += 1
            k = i.partition('title=')[2]
            k = k.partition('>')[0].strip('"')
            print(f'{c}.{k}')
def recom():
    url = 'https://mangareader.to/home'
    r = requests.get(url).content
    soup = BeautifulSoup(r, 'lxml')
    a = soup.find_all('div', {'id': 'manga-featured'})[0]
    a = str(a).split(',')
    c = 0
    print('''
    ----------------------Recommendations----------------------''')
    for i in a:
        if 'title=' in i:
            c += 1
            k = i.partition('title=')[2]
            k = k.partition('>')[0].strip('"')
            print(f'{c}.{k}')
def main():
    while True:
        ch=int(input('''
        1.Trending
        2.Recommendations
        3.Most viewed
        choice:'''))

        if ch==1:trending()
        elif ch==2:recom()
        elif ch==3:
            mvchoice=int(input('''
        ----------------------Most viewed----------------------
        1.today
        2.week
        3.month
        choice:'''))
            if mvchoice==1:mv(0)
            elif mvchoice==2:mv(1)
            elif mvchoice==3:mv(2)
if __name__=='__main__':
    main()