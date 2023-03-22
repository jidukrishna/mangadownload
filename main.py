import time
import manist
import sing
import download
import shutil
import os
import desktopfinder
from rectremo import *
import userwish
import sinpdf
directory = desktopfinder.finddesktop()
os.chdir(directory)
try:
    os.chdir('manga_downloaded')
except:
    os.mkdir('manga_downloaded')
    os.chdir('manga_downloaded')
    with open('readme.txt', 'w') as f:
        f.write('contact me in instagram : https://www.instagram.com/jidukrishnapj/ ')
directory = os.getcwd().replace('\x5c','//')
print(f'working directory {directory}')
try:
    shutil.rmtree('imgs processing',ignore_errors=True)
except:pass
while True:
    os.chdir(directory)
    try:
        shutil.rmtree('imgs processing', ignore_errors=True)
    except:
        pass
    choice = input('''
----------------MANGA DOWNLOADER----------------by @jidukrishnapj on insta
    1.GO TO https://mangakakalot.com/ 
    2.SELECT THE LINK OF THE CHAP U WANT TO DOWNLOAD
    3.OR GO TO THE MAIN PG AND COPY THE LINK TO DOWNLOAD ENTIRE THING


    a.full download
    b.single chap
    c.select chap(eg.click the link for chap 25 and download the next specified chaps )
    d.Trending
    e.Recommendations
    f.Most viewed
    g.exit
    h.compiler one shot
    choice:''')
    try:
        if choice == 'a':
            name = input('manga name:')
            if name in os.listdir():
                ch = input('it will overwrite . so change the name').lower()
            else:
                url = input('url=')
                t1=time.time()
                mangalist = manist.chapl(url)
                print('started takes a long time')

                reply = download.md(mangalist, name,directory)
                t2=time.time()
                print(f'your entire series took {t2-t1}s')
                print(reply)






        elif choice == 'b':
            name = input('manga name(plz put the chap no also):')
            namecheck = f'{name}.pdf'
            if namecheck in os.listdir():
                ch = input('it will overwrite so try again').lower()
            else:
                url = input('url=')
                time1 = time.time()
                imageslink = sing.sim(url)

                print('started')
                reply = download.sd(imageslink, name, directory)
                time2 = time.time()
                print(reply)
                print('the deed is done')
                print('time taken : ', time2 - time1)
                time.sleep(3)




        elif choice=='c':
            name = input('manga name:')
            if name in os.listdir():
                ch = input('it will overwrite . so change the name').lower()
            else:
                url = input('url=')
                chap=int(input('how many chap:'))
                mangalist = userwish.userchap(url,chap)
                print('started takes a long time')
                reply = download.md(mangalist, name, directory)
                print(reply)







        elif choice=='d':trending();enter=input('press enter after reading')

        elif choice=='e':recom();enter=input('press enter after reading')
        elif choice=='f':
            while True:
                mvchoice = int(input('''
                ----------------------Most viewed----------------------
                1.today
                2.week
                3.month
                4.exit
                choice:'''))
                if mvchoice == 1:mv(0)
                elif mvchoice == 2:mv(1)
                elif mvchoice == 3:mv(2)
                elif mvchoice==4:
                    print('exiting in 3 sec')
                    time.sleep(3)
                    break
                else:print('not valid')
                enter = input('press enter after reading')







        elif choice == 'g':
            print('stopping and thank u for using my service')
            time.sleep(3)
            os.system('cls')
            quit()


        elif choice=='h':
            man_dir=input('directory : ').strip().replace('\x5c','//')
            one_shot=input('name of the pdf : ')
            sinpdf.normal_mer(man_dir,one_shot)




        else:
            print('invalid')
        d = input('press enter to continue')
        print('the window will refresh in 2.5 sec')
        time.sleep(3)
        os.system('cls')
    except Exception as e:
        print(f'contact dev with this error {e} or try once more')
        d=input('press enter to continue')


