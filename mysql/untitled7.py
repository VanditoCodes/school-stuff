import mysql.connector
connection = mysql.connector.connect(host = 'localhost'
                                     user = 'root'
                                     passwd = 'Vandit2002'
                                     database = 'ut')
cursor = connection.cursor()