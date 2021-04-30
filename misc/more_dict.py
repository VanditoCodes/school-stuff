l = input("Enter a list: ").split()

d = {}
l1 = len(l) 

for i in l:
    d[i]=l.count(i)
    
print (d)