import requests, img2pdf
import os
import sing
from pypdf import PdfMerger
from tqdm import tqdm
import time, numpy, threading

import shutil


def sd(images, name, d, act=1):
    try:
        os.chdir(d)
        os.mkdir('imgs processing')
        os.chdir('imgs processing')
        kl = images

        c = 1
        imgl = []

        def t1(op1, start):
            c = start + 1
            for i in op1:
                headers = {
                    'referer': f'Referer: {i}'
                }
                global h
                h = headers
                while True:
                    try:
                        r = requests.get(i, headers=headers, timeout=5).content
                        with open(f'{c}.jpg', 'wb') as f:
                            f.write(r)
                        imgl.append(f'{c}.jpg')
                        c += 1
                        break
                    except:
                        time.sleep(1)

        b = numpy.array_split(images, 100)
        for i in b:
            try:
                threading.Thread(target=t1, daemon=True, args=(i, images.index(i[0]))).start()
            except:
                pass

        while True:
            try:

                if threading.active_count() == act:
                    break
                else:
                    time.sleep(0.2)
            except:
                os.chdir(d)
                shutil.rmtree('imgs processing')
                print('fail')
                return

        file_name = f'{d}/{name}.pdf'
        b = {int(i.rstrip('.jpg')): i for i in imgl}
        imgl = [b[i] for i in sorted(b)]
        fop = {j: k for k, j in zip(kl, imgl)}

        with open(file_name, 'wb') as f:
            f.write(img2pdf.convert(imgl))

        os.chdir(d)
        shutil.rmtree('imgs processing', ignore_errors=True)
        return 'success'
    except Exception as e:
        os.chdir(d)
        os.rmdir('imgs processing')

        print(f'contact developer and this mmsg {e}')


def md(list, name, d):
    os.chdir(d)
    os.mkdir(name)
    d = f'{d}//{name}'
    os.chdir(d)
    chap = 1
    opo = time.time()
    for i in tqdm(list):
        imgl = sing.sim(i)
        k = sd(images=imgl, name=str(chap), d=d, act=2)
        chap += 1
    mer = input('''
    
    
    wanna one shot type s to compile to a single pdf:''').lower()
    if mer == 's':

        b = os.listdir()
        b = {int(i.rstrip('.pdf')): i for i in b}
        imgl = [b[i] for i in sorted(b)]
        merger = PdfMerger()
        for i in tqdm(imgl):
            merger.append(i)
        os.mkdir('one-shot')
        os.chdir('one-shot')
        merger.write(f'{name}.pdf')
        merger.close()
        print('u are all finished')

    os.chdir(d)
    opk = time.time()

    return 'success'


def main():
    c = 1


if __name__ == '__main__':
    a = eval(input('url='))
    sd(a, name='helo', d=r'C:\Users\Jidu\OneDrive\Desktop\manga_downloaded\imgs processing')
