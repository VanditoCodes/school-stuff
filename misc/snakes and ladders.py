import random
print("Greetings player! May i know your name?")
name=input("Enter your name: ")
print("Welcome",name,"! Would you like to play a game of snakes and ladders???")
print("Press yes if you want to play, no if you don't want to play : ")
choice=input("Enter your choice : ")
a=0


while choice=="yes":
    roll=random.randint(1,6)
    
    print("do you want to roll the dice???")
    rolldice=input("Enter yes or no: ")
    a=a+int(roll)
    if rolldice=="yes":
        
        print("You rolled",roll,"!")
        
        print("you are now on square no: ",a)
        if a%7==0:
            print("Congratulations! You have reached a ladder! You will now go 11 steps ahead!")
            a+=11
            print("You are now at step:",a)
        if a%13==0:
            print("Congratulations! You have reached a ladder! You will now go 20 steps ahead!")
            a+=20
            print("you are now at step:",a)
        if a==23 or a==37 or a==66 or a==99 or a==15:
            print("Oh no you have reached a snake! You will now go 12 steps behind")    
            a-=12
            print("you are now at step:",a)
        if a>100:
            print("congratulations!! You have won!!!")
            break
    else:
        break
    
    