import threading
import time
import numpy
import requests
import os
import img2pdf
from tqdm import tqdm
def fast(a,dir=os.getcwd()):
    os.chdir(dir)
    c=1
    imgl=[]

    def t1(op1,start):
        c=start+1
        for i in op1:
            headers = {
                'referer': f'Referer: {i}'
            }
            r = requests.get(i, headers=headers).content
            with open(f'{c}.jpg', 'wb') as f:
                f.write(r)
            imgl.append(f'{c}.jpg')
            c += 1
    b=numpy.array_split(a,100)
    for i in (tqdm(b)):
        try:
            threading.Thread(target=t1,args=(i,a.index(i[0]))).start()
        except:pass

    while True:
        if threading.active_count()==2:
            b = {int(i.rstrip('.jpg')): i for i in imgl}
            imgl = [b[i] for i in sorted(b)]

            with open('manga.pdf', 'wb') as f:
                f.write(img2pdf.convert(imgl))

            for i in imgl:
                os.remove(i)
            print('the deed is done')
            print(imgl)
            break
        else:time.sleep(0.2)


a=eval(input('url='))
fast(a,dir=r'C:\Users\Jidu\OneDrive\Desktop\manga_downloaded\imgs processing')





