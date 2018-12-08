print("Jednostka bazowa:")
print("1.Celsjusz")
print("2.Fahrenheit")
print("3.Kelvin")
a=int(input("->"))
b=int(input("Temperatura: "))
if a==1:
    c=b
    f=b*1.8+32
    k=b+273.15
    print("Celsjusz: "+str(c))
    print("Fahrenheit: "+str(f))
    print("Kelvin: "+str(k))
elif a==2:
    c=(b-32)/1.8
    f=b
    k=(b-459)*(5/9)
    print("Celsjusz: "+str(c))
    print("Fahrenheit: "+str(f))
    print("Kelvin: "+str(k))
elif a==3:
    c=b-273.15
    f=(b/1.8)-459
    k=b
    print("Celsjusz: "+str(c))
    print("Fahrenheit: "+str(f))
    print("Kelvin: "+str(k))
