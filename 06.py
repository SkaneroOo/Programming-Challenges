from random import randint
a=int(input('Do ilu punktów chcesz grać? '))
pp=0
hs=0
ep=0
def score(a,b):
	if a>b:
		hs=a
	else:
		hs=b
	return(hs)
while hs!=a:
	print('1. Kamień')
	print('2. Papier')
	print('3. Nożyce')
	p=int(input())
	e=randint(1,3)
	if p==e:
		print('Remis!')
	elif(p==1 and e==3) or (p==2 and e==1) or (p==3 and e==2):
		print('Zdobywasz punkt!')
		pp+=1
		hs=score(pp,ep)
	else:
		print('Przeciwnik zdobywa punkt!')
		ep+=1
		hs=score(pp,ep)
if pp>ep:
	print('Wygrałeś!')
else:
	print('Przegrałeś!')
