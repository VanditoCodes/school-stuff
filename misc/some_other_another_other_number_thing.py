n = int(input("enter n"))
s=0
for i in range (1,n+1):
    s += i/((i+1)**(1/2))    
print(s)