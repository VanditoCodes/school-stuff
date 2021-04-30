import mysql.connector 
connection = mysql.connector.connect (host='localhost',
                                user = 'root',
                                passwd = 'Vandit2002',
                                database = 'ut')
cursor = connection.cursor()

def insertinto():
    Itemcode = input("Enter Item Code: ")
    Itemname = input("Enter Item Name:")
    Price = float(input("Enter Price: "))
    q = ("INSERT INTO item VALUES (('%s'),('%s'),('%f'));" %(Itemcode, Itemname, Price))
    cursor.execute(q)
    connection.commit()

def display():
    q = "SELECT * from item;"
    cursor.execute(q)
    for m in cursor.fetchall():
        print (m)
        
def particular():
    Itemcode = input("Enter particular Item Code:")
    q = ("SELECT * FROM item WHERE Itemcode = '%s';" %(Itemcode))
    cursor.execute(q)
    for m in cursor.fetchall():
        print (m)
        

x = input("Would you like to insert record, display all records or display particular record? [enter a or b or c respectively]: ")

if x == "a":
    insertinto()
elif x == "b":
    display()
elif x == "c":
    particular()
else :
    print ("Kuch galat hai bhau")