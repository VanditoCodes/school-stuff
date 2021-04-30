l = input("Enter a list: ").split()

d = {}
l1 = len(l) 
o = 0
for i in l:
    o += l.count(i)
    d[i]=o
    
print (d)