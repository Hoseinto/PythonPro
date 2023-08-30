n = int (input())
import collections 
d = collections.OrderedDict ()
for i in range (0,n):
    a = input ()
    b = a.split()
    for j in range (1,len (b)):
        d [b[j]] = d.get(b[j],0) + 1

#1111111111111111111111111111111111111

d ['Horror'] = d.get('Horror',0)
d ['Romance'] = d.get('Romance',0)
d ['Comedy'] = d.get('Comedy',0)
d ['History'] = d.get('History',0)
d ['Adventure'] = d.get('Adventure',0)
d ['Action'] = d.get('Action',0)

h = sorted(d.items(), key=lambda x: (-x[1],x[0]), reverse=True)
x = list ()
y = list ()

for i in range (0,len(h)):
    x.append (h[i][0])

for j in range (0,len(h)):
    y.append (h[j][1])

for i in range (0,6):
    print ('%s : %s' %( x[5-i], y[5-i]))