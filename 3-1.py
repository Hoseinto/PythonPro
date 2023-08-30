import mysql.connector 

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='first')

cursor = cnx. cursor ()
query = 'SELECT * FROM table1;'
cursor.execute (query)

List = list ()

for (Name, Weight, Height) in cursor:
    List.append ((Name, Weight, Height))

cnx.close ()

List.sort (key=lambda x:x[2],reverse = True)
l = list ()
i = 0
n = len (List)

while i < n:
    if len (List) > 1 :
        if List [0][2] != List [1][2]:
            print ('%s %i %i' %(List [0] [0],List [0] [1],List [0] [2]))
            List.remove (List [0])
            i += 1
        else:
            j = 2
            l.append (List [0])
            l.append (List [1])
            i += 2
            while j < (len(List)):
                if List [0][2] == List [2][2]:
                    l.append (List [2])
                    List.remove (List [2])
                    i += 1
            l.sort (key=lambda x:x[1])
            for k in l:
                print ('%s %i %i' %(k [0],k [1],k [2]))
            l.clear ()
            List.remove (List [1])
            List.remove (List [0])
    else:
        print ('%s %i %i' %(List [0] [0],List [0] [1],List [0] [2]))
        i += 1