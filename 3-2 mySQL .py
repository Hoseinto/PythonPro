import mysql.connector 
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check (email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
    

email = input ('Email: ')

while check (email) != True:
    email = input ('Email format is incorrect. Please enter your email based on following pattern: Username@email.com: \n')


password = input ('Password: ')

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='first')

cursor = cnx. cursor ()
cursor.execute ('INSERT INTO table VALUES (%s, %s)' % (email,password))
cnx.commit ()
cnx.close ()