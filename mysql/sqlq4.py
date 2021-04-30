import mysql.connector
connection = mysql.connector.connect (host = 'localhost',
                                      user = 'root',
                                      passwd = 'Vandit2002',
                                      database = 'ut')

cursor = connection.cursor()

def insertinto():
    Rollno= int(input("Insert Roll Number: "))
    Name= input("Naam bata bhai: ")
    Class= int(input("Class bata bhai: "))
    DOB= int(input("Date bata"))
    Gender = input("Gender bata ")
    q = ("INSERT INTO student VALUES(('%s'),('%s'),('%f'),('%f'),('%s'));" %(Rollno,Name,Class,DOB,Gender))
    cursor.execute(q)
    connection.commit()

def update():
    Rollno=int(input("Roll Number to update: "))
    Name= input("Naam update: ")
    Class= int(input("Class update: "))
    DOB= int(input("Date update"))
    Gender=input("Gender update ")
    q = ("UPDATE student set Name='%s',Class='%s',DOB='%s',Gender='%s' where Rollno='%f';") %(Name,Class,DOB,Gender,Rollno)    
    cursor.execute(q)
    connection.commit()

x = input("Enter bale balle [a or b]")
    
if x == "a":
    insertinto()
elif x == "b":
    update()    