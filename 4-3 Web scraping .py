import re
from bs4 import BeautifulSoup
from selenium import webdriver
import mysql.connector 

#selenium+one more scroll

n = input ()

#please do not enter anything because the website hasn't been classified well
driver = webdriver.Firefox()
driver.get ('https://karnameh.com/buy-used-cars/%s'% (n))
driver.execute_script("window.scrollTo(0, 1080)")

#finding value and km with soup

soup = BeautifulSoup (driver.page_source, 'html.parser')
value = soup.find_all ('p', attrs = {'class':['inspected-car-card__bottom-text']})
km = soup.find_all ('div',attrs = {'class':['kt-text-truncate']})

#add value and km in 2 list

value_list = list ()
km_list = list ()

for i in range (0,len (value)):
    value_list.append (value [i].text)

for i in range (0,len (km)):
    if 'کیلومتر' in km[i].text:
        km_list.append (km [i].text)

#Database:
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='first')

cursor = cnx.cursor ()
for i in range (0,len (value_list)):
    cursor.execute ('INSERT INTO carrr VALUES (%s, %s)' % (value_list [i], km_list [i]))
    cnx.commit ()

cnx.close ()