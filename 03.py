from datetime import date
dm=0
rok=date.today().year
miesiąc=date.today().month
dzień=date.today().day
mies=[-1,3,0,3,2,3,2,3,3,2,3,2,3]
r=int(input('Rok w którym się urodziłeś: '))
m=int(input('Miesiąc w którym się urodziłeś: '))
d=int(input('Dzień w którym się urodziłeś: '))
if miesiąc>m:
    for x in range(m,miesiąc):
        dm+=mies[x]
else:
    for x in range(miesiąc,m):
        dm+=mies[x]
a=((rok-r)*365+(miesiąc-m)*28+dzień-d+dm)
a=a*86400
for x in range(r,rok):
    if x%4==0:
        a+=86400
print(a)
