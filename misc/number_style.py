n = int(input("Enter number of rows: "))

def pasctri(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new = [1]
        result = pasctri(n-1)
        prev = result[-1]
        for i in range(len(prev)-1):
            new.append(prev[i] + prev[i+1])
        new += [1]
        result.append(new)
    return result

for i in pasctri(n):
    for j in i:
        print(j, end=" ")
    print()