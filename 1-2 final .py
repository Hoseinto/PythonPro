iran = [0, 0, 0, 0, 0]
spain = [0, 0, 0, 0, 0]
port = [0, 0, 0, 0, 0]
mor = [0, 0, 0, 0, 0]
#11111111111111111111111111111111111111111
a = input ()
b = a.split ('-')
b [0] = int (b[0])
b [1] = int (b[1])
iran [3] += (b[0] - b[1])
spain [3] += (b[1] - b[0])
if b[0]>b[1]:
    iran [4] += 3
    iran [0] += 1
    spain [1] += 1
elif b[0]<b[1]:
    spain [4] += 3
    spain [0] += 1
    iran [1] += 1
else:
    iran [4] += 1
    iran [2] += 1
    spain [4] += 1
    spain [2] += 1

#22222222222222222222222222222222222222222222222
a = input ()
b = a.split ('-')
b [0] = int (b[0])
b [1] = int (b[1])
iran [3] += (b[0] - b[1])
port [3] += (b[1] - b[0])
if b[0]>b[1]:
    iran [4] += 3
    iran [0] += 1
    port [1] += 1
elif b[0]<b[1]:
    port [4] += 3
    port [0] += 1
    iran [1] += 1
else:
    iran [4] += 1
    iran [2] += 1
    port [4] += 1
    port [2] += 1

#3333333333333333333333333333333333333333333333
a = input ()
b = a.split ('-')
b [0] = int (b[0])
b [1] = int (b[1])
iran [3] += (b[0] - b[1])
mor [3] += (b[1] - b[0])
if b[0]>b[1]:
    iran [4] += 3
    iran [0] += 1
    mor [1] += 1
elif b[0]<b[1]:
    mor [4] += 3
    mor [0] += 1
    iran [1] += 1
else:
    iran [4] += 1
    iran [2] += 1
    mor [4] += 1
    mor [2] += 1

#444444444444444444444444444444444444444444444444
a = input ()
b = a.split ('-')
b [0] = int (b[0])
b [1] = int (b[1])
spain [3] += (b[0] - b[1])
port [3] += (b[1] - b[0])
if b[0]>b[1]:
    spain [4] += 3
    spain [0] += 1
    port [1] += 1
elif b[0]<b[1]:
    port [4] += 3
    port [0] += 1
    spain [1] += 1
else:
    spain [4] += 1
    spain [2] += 1
    port [4] += 1
    port [2] += 1

#555555555555555555555555555555555555555555555555555
a = input ()
b = a.split ('-')
b [0] = int (b[0])
b [1] = int (b[1])
spain [3] += (b[0] - b[1])
mor [3] += (b[1] - b[0])
if b[0]>b[1]:
    spain [4] += 3
    spain [0] += 1
    mor [1] += 1
elif b[0]<b[1]:
    mor [4] += 3
    mor [0] += 1
    spain [1] += 1
else:
    spain [4] += 1
    spain [2] += 1
    mor [4] += 1
    mor [2] += 1

#66666666666666666666666666666666666666666666666666666
a = input ()
b = a.split ('-')
b [0] = int (b[0])
b [1] = int (b[1])
port [3] += (b[0] - b[1])
mor [3] += (b[1] - b[0])
if b[0]>b[1]:
    port [4] += 3
    port [0] += 1
    mor [1] += 1
elif b[0]<b[1]:
    mor [4] += 3
    mor [0] += 1
    port [1] += 1
else:
    port [4] += 1
    port [2] += 1
    mor [4] += 1
    mor [2] += 1

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

port.append ('Portugal')
spain.append ('Spain')
mor.append ('Morocco')
iran.append ('Iran')

all = [iran, spain, port, mor]
Jadval = sorted (all, key = lambda x: int(x[4]))
Jadval_1 = list ()
Jadval_11 = list ()
Jadval_111 = list ()

if Jadval [3][4] != Jadval [2][4]:
    print ('%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' %(Jadval[3][5],Jadval[3][0],Jadval[3][1],Jadval[3][2],Jadval[3][3],Jadval[3][4]))
    all.clear ()
    all. append (Jadval [0]) 
    all. append (Jadval [1]) 
    all. append (Jadval [2]) 
else:
    Jadval_1 = Jadval [2:]
    Jadval_11 = sorted (Jadval_1, key = lambda x: int(x[3]))
    if Jadval_11 [0][3] != Jadval_11[1][3]:
        print ('%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' %(Jadval_11[1][5],Jadval_11[1][0],Jadval_11[1][1],Jadval_11[1][2],Jadval_11[1][3],Jadval_11[1][4]))
        all.clear ()
        all. append (Jadval [0]) 
        all. append (Jadval [1])
        all. append (Jadva_11 [0])
    else:
        Jadval_111 = sorted (Jadval_1, key = lambda x: str(x[5]))
        print ('%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' %(Jadval_111[0][5],Jadval_111[0][0],Jadval_111[0][1],Jadval_111[0][2],Jadval_111[0][3],Jadval_111[0][4]))
        all.clear ()
        all.append (Jadval [0])
        all.append (Jadval [1])
        all.append (Jadval_111 [1]) 

#1111111111111111111111111111111111111111111111111111111111111111111111111111

Jadval.clear ()
Jadval_1.clear ()
Jadval_11.clear ()
Jadval_111.clear ()
Jadval = sorted (all, key = lambda x: int(x[4]))

if Jadval [1][4] != Jadval [2][4]:
    print ('%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' %(Jadval[2][5],Jadval[2][0],Jadval[2][1],Jadval[2][2],Jadval[2][3],Jadval[2][4]))
    all.clear ()
    all.append (Jadval [0])
    all.append (Jadval [1])
else:
    Jadval_1 = Jadval [1:]
    Jadval_11 = sorted (Jadval_1, key = lambda x: int(x[3]))
    if Jadval_11 [0][3] != Jadval_11[1][3]:
        print ('%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' %(Jadval_11[1][5],Jadval_11[1][0],Jadval_11[1][1],Jadval_11[1][2],Jadval_11[1][3],Jadval_11[1][4]))
        all.clear ()
        all. append (Jadval [0]) 
        all. append (Jadval_11 [0])
    else:
        Jadval_111 = sorted (Jadval_1, key = lambda x: str(x[5]))
        print ('%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' %(Jadval_111[0][5],Jadval_111[0][0],Jadval_111[0][1],Jadval_111[0][2],Jadval_111[0][3],Jadval_111[0][4]))
        all.clear ()
        all.append (Jadval [0])
        all.append (Jadval_111 [1])

#22222222222222222222222222222222222222222222222222222222222222222222222222222

Jadval.clear ()
Jadval_1.clear ()
Jadval_11.clear ()
Jadval_111.clear ()
Jadval. append (all[0])
Jadval. append (all[1])

if Jadval [1][4] != Jadval [0][4]:
    print ('%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' %(Jadval[1][5],Jadval[1][0],Jadval[1][1],Jadval[1][2],Jadval[1][3],Jadval[1][4]))
    all.clear ()
    all. append (Jadval [0]) 
else:
    Jadval_1 = Jadval [1:]
    Jadval_11 = sorted (Jadval_1, key = lambda x: int(x[3]))
    if Jadval_11 [0][3] != Jadval_11[1][3]:
        print ('%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' %(Jadval_11[1][5],Jadval_11[1][0],Jadval_11[1][1],Jadval_11[1][2],Jadval_11[1][3],Jadval_11[1][4]))
        all.clear ()
        all. append (Jadval_11 [0]) 
    else:
        Jadval_111 = sorted (Jadval_1, key = lambda x: str(x[5]))
        print ('%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' %(Jadval_111[0][5],Jadval_111[0][0],Jadval_111[0][1],Jadval_111[0][2],Jadval_111[0][3],Jadval_111[0][4]))
        all.clear ()
        all.append (Jadval_111 [1])

print ('%s wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' %(all [0][5],all [0][0],all [0][1],all [0][2],all [0][3],all [0][4]))


