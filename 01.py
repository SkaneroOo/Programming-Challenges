from random import randint
a=randint(1,100)
print('Odgadnij liczbę od 1 do 100')
b=int(input())
c=1
while a!=b:
	if b<a:
		print('Za mało')
		b=int(input())
		c+=1
	elif b>a:
		print('Za dużo')
		b=int(input())
		c+=1
print('Wygrałeś za '+str(c)+' razem.')