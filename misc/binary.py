import math
l = input("ENter list:").split() 
l = list(map(int,l))
l.sort()
x = int(input("ENter Number to search: "))
k = math.inf
m=0
j=0
while (j!=x):
    if (x== l[len(l)//2]):
        k = len(l)//2
        j = l[k]
    if (x< l[(len(l)//2)]):
         m+= ((len(l))//2)
         l = l[0:(len(l))//2]
    if (x> l[(len(l)//2)]):
         m+= (len(l)-(len(l))//2)
         l = l[(len(l))//2:len(l)]
         
print (m)
    
         