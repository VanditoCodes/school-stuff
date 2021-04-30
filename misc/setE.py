s = (input("Enter your string: "))
l = s.split()
print (len(l))
s1 = ""
for i in range (0,len(l)-1):
    s1 += l[i]+l[i+1]
    s1 += " "
        
print(s1)    
        
        