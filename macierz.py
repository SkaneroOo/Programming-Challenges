from math import *
dict={
    'x':0,
    'y':0,
    'list':[]
}

def printer(dict):
    zmienna=''
    for a in range(0,dict['y']):
        for b in range(0,dict['x']):
            zmienna+='['+dict['list'][a*dict['y']+b]+']'
        print(zmienna)
        zmienna=''

def create(dict):
    dict['x']=int(input('X >>>'))
    dict['y']=int(input('Y >>>'))
    for a in range(0,dict['x']*dict['y']):
        dict['list']+=input()
    printer(dict)
    print('Czy chcesz zatwierdzić tą macierz (tak/nie)?')
    a=input('>>>')
    if a=='tak':
        print('Macierz została zatwierdzona')
        return dict
    else:
        dict = {
            'x': 0,
            'y': 0,
            'list': []
        }
        create(dict)

def wyznacznik(dict):
    var=dict['x']
    r=0
    l=0
    temp=1
    for a in range(0,var):
        for b in range(0,var):
            temp=temp*int(dict['list'][var*a+b])
        r+=temp
        temp=1
    for a in range(0,var):
        for b in range(0,var):
            temp=temp*int(dict['list'][var*a-var+b])
        l+=temp
        temp=1
    print('Wyznacznik wynosi '+str(r-l))

while True:
    create(dict)
    if dict['y']==dict['x']:
        wyznacznik(dict)