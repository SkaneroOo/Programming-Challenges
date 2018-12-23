x=int(input('Do ilu: '))
for a in range(1,x+1):
    if a%3==0 and a%5==0:
        print('Fizz Buzz')
    elif a%3==0:
        print('Fizz')
    elif a%5==0:
        print('Buzz')
    else:
        print(a)
