n = int(input("Enter a number plss : "))
s = 0
p = 1
m = n
while n>0:
    digit = n%10
    s += digit 
    n = n//100
    
m//10

while m>0:
    digit = m%10
    p *= digit
    m = m//100

print (s,p,s+p)    