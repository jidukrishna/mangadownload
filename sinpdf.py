import os
from pypdf import PdfMerger
from tqdm import tqdm
def normal_mer(dir,name):
    try:
        merger=PdfMerger()
        os.chdir(dir.replace('\x5c','//'))
        b = os.listdir()
        b = {int(i.rstrip('.pdf')): i for i in b}
        imgl = [b[i] for i in sorted(b)]
        for i in tqdm(imgl):
            merger.append(i)
        os.mkdir('one-shot')
        os.chdir('one-shot')
        merger.write(f'{name}.pdf')
        merger.close()
        print('successful')
        return
    except:
        print('fail')
        return


