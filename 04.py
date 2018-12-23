szyfr=['a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n','ń','o','ó','p','q','r','s','ś','t','u','v','w','x','y','z','ż','ź']
print('1. Zaszyfruj')
print('2. Odszyfruj')
z=int(input())
e=''
if z==1:
    b=input('Wprowadź wyraz do zaszyfrowania ')
    b=b.lower()
    c=list(b)
    for d in range(0,len(c)):
        temp=szyfr.index(c[d])
        if temp==34:
            temp-=35
        e=e+szyfr[temp+1]
elif z==2:
    b=input('Wprowadź wyraz do odszyfrowania ')
    b=b.lower()
    c=list(b)
    for d in range(0,len(c)):
        temp=szyfr.index(c[d])
        e=e+szyfr[temp-1]
print(e)
