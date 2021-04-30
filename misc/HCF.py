a = int(input("enter a number: "))
b= int(input("enter a number: "))

while a!=b:
    if a>b:
        a = a-b
    elif b>a:
        b = b-a

else :
    print ("HCF is", a)