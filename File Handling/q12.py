f = open("f.txt","w")
f.write("Neither apple nor pine are in pineapple.......................\n.................going on \n lalalalalalal")
f.close()

f = open("f.txt","r+")
print(f.read())
f.write("\nd computer science")
a=0
f.seek(0)
for i in f.readlines():
    a+=1
    print(a,":",i)
f.seek(0)
print(f.readlines()[-1])
f.seek(9)
print(f.readline())

f.seek(0)
x = int(input("whassa number"))
print(f.readlines()[x-1])

f.seek(0)

d={}
for i in f.readlines():
    for j in i.split():
        if j[0].lower() in d:
            d[j[0].lower()]+=1
        else:
            d[j[0].lower()]=1
print(d)