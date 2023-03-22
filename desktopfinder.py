import os

def finddesktop():

    user=os.environ['USERPROFILE']
    target=f'{user}\Desktop'.replace('''\ ''','''/''')
    try:
        os.chdir(target)
        d=target
        return d
    except:pass
    try:
        dire=f'{user}\OneDrive\Desktop'.replace('''\ ''','''/''')
        os.chdir(dire)
        d=dire
        return d
    except:pass
