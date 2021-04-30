r = {"Lisa":"Daughter", "Bart":"son","Marge":"mother","Homer":"father", "Santa":"dog"}
a = {"Lisa":8, "Bart":10,"Marge":35,"Homer":40, "Santa":2}

for i in r:
    print (i, "is a ", r[i], "and is ", a[i], "years old"  )
    
print(r.values())