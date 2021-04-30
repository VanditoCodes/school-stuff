l = input("ENter Numbers: ").split()
l = list(map(int,l))
n = len(l)
for i in range (0,n):
    for j in range (0,i):
        if l[i]<l[j]:
            l[i] = l[j]
            
print(l)