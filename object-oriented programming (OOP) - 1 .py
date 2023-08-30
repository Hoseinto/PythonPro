
class StudentA:
    count = 0
    age_total = 0
    height_total = 0
    weight_total = 0
    def __init__(self, age,height,weight):
        self.age = age
        self.height = height
        self.weight = weight
        StudentA.age_total += self.age
        StudentA.height_total += self.height
        StudentA.weight_total += self .weight
        StudentA.count += 1
    def average ():
        print (float (StudentA.age_total/StudentA.count))
        print (float (StudentA.height_total/StudentA.count))
        print (float (StudentA.weight_total/StudentA.count))
    def HH ():
        return (float (StudentB.height_total/StudentA.count))

class StudentB ():
    count = 0
    age_total = 0
    height_total = 0
    weight_total = 0
    def __init__(self, age,height,weight):
        self.age = age
        self.height = height
        self.weight = weight
        StudentB.age_total += self.age
        StudentB.height_total += self.height
        StudentB.weight_total += self .weight 
        StudentB.count += 1
    def average ():
        print (float (StudentB.age_total/StudentB.count))
        print (float (StudentB.height_total/StudentB.count))
        print (float (StudentB.weight_total/StudentB.count))
    def HH ():
        return (float (StudentB.height_total/StudentB.count))
    


n = int (input())
a = input()
aa = a.split ()
A = list (map (lambda x: float (x), aa))
h = input ()
hh = h.split ()
H = list (map (lambda x: float (x), hh))
w = input ()
ww = w.split ()
W = list (map (lambda x: float (x), ww))
ClassA = list ()

for i in range (0,n):
    ClassA.append (StudentA (A[i], H[i],W [i]))


n = int (input())
a = input()
aa = a.split ()
A = list (map (lambda x: float (x), aa))
h = input ()
hh = h.split ()
H = list (map (lambda x: float (x), hh))
w = input ()
ww = w.split ()
W = list (map (lambda x: float (x), ww))
ClassB = list ()

for i in range (0,n):
    ClassB.append (StudentB (A[i], H[i],W [i]))

StudentA.average()
StudentB.average()

x = StudentA.HH ()
y = StudentB.HH ()

if x > y:
    print ('A')
elif x < y:
    print ('B')
else:
    print ('Same')    