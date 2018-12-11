from random import randint
a=[-1,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.',',','!','?','/',':',';']
b=randint(8,24)
c=len(a)-1
d=''
while b!=0:
	e=randint(1,c)
	d+=a[e]
	b-=1
print(d)
