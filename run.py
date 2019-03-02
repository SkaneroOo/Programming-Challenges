from math import *
hi = []
calc = []
with open("Data\hi.txt") as file:
    for line in file: 
        line = line.strip()
        hi.append(line)
with open("Data\calc.txt") as file:
    for line in file: 
        line = line.strip()
        calc.append(line)

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
