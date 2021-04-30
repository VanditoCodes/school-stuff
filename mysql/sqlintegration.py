import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',
                               user = 'root',
                               passwd = 'Vandit2002'
                               )
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for l in mycursor:
    print (l)

mycursor.close()
mydb.close()

