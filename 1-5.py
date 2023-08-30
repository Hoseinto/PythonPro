
n = input ()
m = 0
x = 0
a = n.split ('.')
for i in range (0, len (a)):
    m += 1
    b = a [i].split ()
    for j in range (1,len (b)):
        m+=1
        if b[j][0].isdigit () == False:
            if b[j][0] == b[j][0].upper () : 
                x += 1
                if b [j][len (b[j])-1] != ',':
                    print ('%i:%s'%(m,b[j]))
                else:
                    x = len (b[j])
                    b [j] = b[j][:(x-1)]
                    print ('%i:%s'%(m,b[j]))


if x ==0 :
    print ('None')