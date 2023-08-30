n = int (input())
f = list ()
m = list ()
for i in range (0,n):
    a = input ()
    b = a.split ('.')
    b [1] = b [1][0].upper () + b [1][1:].lower ()
    if b [0] == 'f':
        f.append (b)
    else:
        m.append (b)

ff = sorted (f,key = lambda x: str(x[1]))
mm = sorted (m,key = lambda x: str(x[1]))
for i in range (0,len(ff)):
    print ('%s %s %s'%(ff[i][0], ff[i][1], ff[i][2]))

for j in range (0,len(mm)):
    print ('%s %s %s'%(mm[j][0], mm[j][1], mm[j][2]))


