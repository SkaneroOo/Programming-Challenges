from turtle import *
from math import *
def setting ():
    color('red','yellow')
    ht()
    speed(25)
    setpos(-500,0)
    setpos(500,0)
    setpos(0,0)
    setpos(0,-500)
    setpos(0,500)
    setpos(0,0)
    penup()
    pencolor('black')
    pensize(3)
a=input('Funkcja od X czy Y?: ')
if a=='x' or a=='X':
    c='f(x)'
elif a=='y' or a=='Y':
    c='f(y)'
b=input(c+'=')
if c=='f(x)':
    setting()
    setpos(-500,0)
    pendown()
    x=xcor()
    while x!=501:
        y=eval(b)
        setpos(x,y)
        x+=1
elif c=='f(y)':
    setting()
    setpos(0,-500)
    pendown()
    y=ycor()
    while y!=501:
        x=eval(b)
        setpos(x,y)
        y+=1
