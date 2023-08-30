def Avval (n):
    c = 0
    for i in range (1,n):
        if n % i == 0:
            c += 1
    if c == 1:
        return ("Good")

a = list ()
b = list ()
for i in range (0,10):
    n = int (input ())
    x = 0
    for j in range (1,n+1):
        if n % j == 0 and Avval (j) == 'Good':
            x = x + 1
    a . append (n)
    b . append (x)
z = a [0]
y = b [0]
for i in range (1,10):
    if b [i] > y:
        z = a [i]
        y = b [i]
    elif b [i] == y:
        if a [i] > z:
            z = a [i]
            y = b [i]
print (z,y)