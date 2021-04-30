s = str(input("Enter something: "))

l = (len(s))//2
x = -1
for i in range(0,l+1):
    if s[i]==s[x]:
        x-=1    
    else :
        print("not a palindrome")
        break
else : 
     print ("Palindrome confirmed")   
        