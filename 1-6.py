n = int (input ())
d = dict()
for i in range (0,n):
    a = input ()
    b = a.split ()
    d [b[1]] = b [0]
    d [b[2]] = b [0]
    d [b[3]] = b [0]

x = input ()
y = x.split ()
for j in range (0,len (y)):
    y [j] = d.get (y[j], y[j])

z = y [0]
for k in range (1, len(y)):
    z = z + ' ' + y [k]

print (z)