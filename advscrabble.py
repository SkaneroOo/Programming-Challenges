from random import randint
a={'a':2,'ą':1,'b':4,'c':2,'ć':3,'d':1,'e':1,'ę':4,'f':6,'g':2,'h':1,'i':4,'j':1,'k':5,'l':2,'ł':3,'m':2,'n':1,'ń':3,'o':3,'ó':1,'p':2,'q':3,'r':1,'s':1,'ś':3,'t':2,'u':2,'v':5,'w':1,'x':3,'y':2,'z':3,'ż':2,'ź':5}
chars=[-1,'A','Ą','B','C','Ć','D','E','Ę','F','G','H','I','J','K','L','Ł','M','N','Ń','O','Ó','P','Q','R','S','Ś','T','U','V','W','X','Y','Z','Ż','Ź']
pc1=[]
pc2=[]
c=[]
e=0
ps1=0
ps2=0
hscore=0
def hs(p1,p2):
	if p1>p2:
		hscore=p1
	else:
		hscore=p2
		return hscore
while len(pc1)==10 and len(pc2)==10:
	pc1+=chars[randint(1,len(chars)-1)]
	pc2+=chars[randint(1,len(chars)-1)]
while hscore>=250:
	e=0
	c=[]
	print('GRACZ 1')
	print('Dostępne litery:')
	print(pc1)
	b=input('Wprowadź wyraz ')
	if b=='':
		pc1+=chars[randint(1,len(chars)-1)]
	elif b.find(' '):
		print('JEDEN WYRAZ!!!')
		b=input('Wprowadź wyraz ')
		b=b.lower()
		c=list(b)
		for d in range(1,len(c)+1):
			if a[c[d-1]].find(pc1)==1:
				e=e+a[c[d-1]]
				print(e)
				ps1+=e
				hscore=hs(ps1,ps2)
				pc1+=chars[randint(1,len(chars)-1)]
			else:
				print('Użyj tylko dostępnych liter.')
				print('Utrata kolejki.')
				pc1+=chars[randint(1,len(chars)-1)]
	e=0
	c=[]
	print('GRACZ 2')
	print('Dostępne litery;')
	print(pc2)
	b=input('Wprowadź wyraz ')
	if b=='':
		pc2+=chars[randint(1,len(chars)-1)]
	elif b.find(' '):
		print('JEDEN WYRAZ!!!')
		b=input('Wprowadź wyraz ')
		b=b.lower()
		c=list(b)
		for d in range(1,len(c)+1):
			if a[c[d-1]].find(pc2)==1:
				e=e+a[c[d-1]]
				print(e)
				ps2+=e
				hscore=hs(ps1,ps2)
				pc2+=chars[randint(1,len(chars)-1)]
			else:
				print('Użyj tylko dostępnych liter.')
				print('Utrata kolejki.')
				pc2+=chars[randint(1,len(chars)-1)
if (ps1>ps2):
	print('Wygrywa gracz 1.')
else:
	print('Wygrywa gracz 2.')