l = input("Enter list: ").split()
l = list(map(int, l))
n = len(l)
for i in range (len(l)):
    for j in range (i,0,-1):
        if l[j]<l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]

print (l)        
    
        