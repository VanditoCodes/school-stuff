import math
n = int(input("Kitne line chahiye bhiaya "))
for i in range(0,n+1):
    print(" "*(n-i), end= "")
    for j in range (0,i+1):
            print(int(math.factorial(i)/(math.factorial(i-j)*math.factorial(j))), end = " 15")
            if j == i:
                print()
                