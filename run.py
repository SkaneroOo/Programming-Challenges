from math import *
from random import randint
import urllib.request
try:
    qhi=[line.strip() for line in open("Data/Questions/hi.txt", 'r')]
    calc=[line.strip() for line in open("Data/Questions/calc.txt", 'r')]
    ahi=[line.strip() for line in open("Data/Answers/hi.txt", 'r')]
except FileNotFoundError:
    print('Przygotowywanie wstępnej konfiguracji...')
    url1='https://pastebin.com/raw/pxfnYRTr'
    url2='https://pastebin.com/raw/6C8KKdkB'
    url3='https://pastebin.com/raw/qtVKPm0F'
    urllib.request.urlretrieve(url1, 'Data/Questions/calc.txt')
    urllib.request.urlretrieve(url2, 'Data/Questions/hi.txt')
    urllib.request.urlretrieve(url3, 'Data/Answers/hi.txt')
    print('Konfiguracja przebiegła pomyślnie.')
    qhi=[line.strip() for line in open("Data/Questions/hi.txt", 'r')]
    calc=[line.strip() for line in open("Data/Questions/calc.txt", 'r')]
    ahi=[line.strip() for line in open("Data/Answers/hi.txt", 'r')]

while True:
    ui=input(">>> ")
    ui=ui.lower()
    if ui in qhi:
        print (ahi[randint(0,len(ahi)-1)])
    elif ui in calc:
        arg=input('Co mam policzyć >>> ')
        print(eval(arg))
    else:
        print ('Przepraszam, nie rozumiem')
