import requests
from bs4 import BeautifulSoup
def userchap(url,chap):
    chaplist=[]
    a=url.split('/')
    a.pop()
    newurl='/'.join(a)
    r=requests.get(newurl)
    soup=BeautifulSoup(r.content,'lxml')
    b=soup.find_all('li',class_='a-h')
    b=str(b).split()
    for i in b:
        if i.startswith('href='):
            op=i.lstrip('href=').rstrip('>').strip('''"''')
            chaplist.append(op)
    orderedcl=chaplist[::-1]
    index=orderedcl.index(url)
    end=index+chap
    if end>len(orderedcl):
        end=len(orderedcl)
    orderedcl=orderedcl[index:end]
    return orderedcl
def main():
    c=1
if __name__=='__main__':
    main()