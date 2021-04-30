from random import randint
n = randint(1,20)

no = int(input("Take a guess"))
count = 0
while no != n:
    if no< n:
        print ("Your guess is too low")
    elif no>n:
        print ("Your guess too high")
    count += 1
    no = int(input("Take a guess"))
else :
    print("Congratulations! u guessed the number in ", (count+1), "guesses!")