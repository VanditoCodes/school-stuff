n = input("Enter ISBN number: ")
s = 0
for i in range (0,10):
    s+= float(n[i]*i)
    
if s%11 == 0:
    print("Valid isbn boi")
else:
    print("invalid, try again ")     