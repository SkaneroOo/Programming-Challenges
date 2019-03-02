from math import *
from random import randint
import urllib.request
try:
    hi=[line.strip() for line in open("Data\hi.txt", 'r')]
    calc=[line.strip() for line in open("Data\calc.txt", 'r')]
#    joke=[line.strip() for line in open("Data\joke.txt", 'r')]
#    jokes=[line.strip() for line in open("Data\jokes.txt", 'r')]
except FileNotFoundError:
    print('Przygotowywanie wstępnej konfiguracji...')
    url1='https://pastebin.com/raw/pxfnYRTr'
    url2='https://pastebin.com/raw/6C8KKdkB'
    urllib.request.urlretrieve(url1, 'Data/calc.txt')
    urllib.request.urlretrieve(url2, 'Data/hi.txt')

while True:
    ui=input(">>> ")
    ui=ui.lower()
    if ui in hi:
        print ('Witaj')
    elif ui in calc:
        calcin=input('Co mam policzyć >>> ')
        print(eval(calcin))
    else:
        print ('Przepraszam, nie rozumiem')
