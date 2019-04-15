from random import randint
bot=list(str(randint(1000,9999)))
player=[]
test=0
while True:
    while bot!=player:
        player=[]
        player=list(input('>>>'))
        for a in range(0,4):
            if player[a]==bot[a]:
                test+=1
        print('*'*test)
        test=0
    print('Gratulacje! Wygrałeś!')
    bot=[]
print(bot)