from datetime import date
n = '1995/09/25'
x = n.split ('/')
BD = list (map (lambda z: int (z),x))
Birth_date = date (BD[0], BD [1], BD [2])
Today = date.today ()
if BD[1] > 12 or BD [2] > 31 or Today < Birth_date:
    print ('WRONG')
else:
    years = Today.year - Birth_date.year
    if (Today - Birth_date.replace(year=Today.year)).days >= 0:
        print (years)
    else:
        age = years - 1
        print (years)