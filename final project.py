import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import mysql.connector
from sklearn import tree


driver = webdriver.Chrome()
url = 'https://bama.ir/car'
driver.get(url)
scroll_times = 20
for i in range(scroll_times):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

html = driver.page_source

driver.close()

soup = BeautifulSoup (html,'html.parser')

#step1 : extracting Data

m = soup.find_all ('p',attrs= {'class':['bama-ad__title']})
other = soup.find_all ('div',attrs= {'class':['bama-ad__detail-row']})
P_A = soup.find_all ('div',attrs= {'class':['bama-ad__price-row']} )



#step2: making lists

model = []
for i in range (0,len(m)):
  model.append (m[i].text.strip ())
#other = year + km + motor and needs to be sorted
year = []
km = []
motor = []
for i in range (0,len (other)):
    o = other[i].text.split ('\n')
    year.append (o[1].strip ())
    km.append (o[3].strip ())
    motor.append (o[5].strip ())
#P_A = price and adress
price = []
address = []
for i in range (0,len(P_A)):
    p = P_A[i].text.split ('\n')
    if 'توافقی' in P_A[i].text:
        price.append (p[2].strip ())
        address.append (p[1].strip ())
    elif len (p) <3:
        price.append (p[3].strip ())
        address.append (p[1].strip ())
    else:
        price.append (p[2].strip ())
        address.append (p[1].strip ())



#step 3: add to database 

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='project')

cursor = cnx.cursor ()
for i in range (0,len (model)):
    cursor.execute ('INSERT IGNORE INTO jadi VALUES (%s, %s, %s, %s, %s, %s)' % (model[i], year [i], km [i], motor [i], price [i], address [i]))
    cnx.commit ()

cnx.close ()

#step 4: reading from database

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='project')

cursor = cnx.cursor ()
x = []
y = []

query = 'SELECT * FROM jadi'
cursor.execute (query)

for (model, year, km, motor, price, address) in cursor:
    x.append ([model, year, km, motor, price])
    y.append ([address])

#step 5 : ML

clf = tree.DecisionTreeClassifier ()
clf = clf.fit (x,y)

mmodel = input ('what is your the model of your car?  ')
yyear = input ('what is the production year of your car?')
kkm = input ('How much has worked your car untill today? ')
mmotor = input ('Please tell us about deatails of the motor of your car.')
pprice = input ('How much do you want to sell it (in Rials) ? Please comma every 3 digits like the example : 1,234,000,000')

new_data = [(mmodel, yyear, kkm, mmotor,pprice)]
answer = clf.predict (new_data)
print ('You are probably coming from %s' % (answer [0]))