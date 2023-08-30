import random
n = input ()
List = n.split ('-')

class Human:
    count = 0
    def __init__(self, name):
        self.name = name
        Human.count += 1

class Footbalist (Human):
    A = 0
    B = 0
    def Team (self):
        if Footbalist.A < 11 and Footbalist.B <11:
            n = random.randint (1,2)
            if n == 1:
                Footbalist.A += 1
                return 'A'
            else:
                Footbalist.B += 1
                return 'B'
        elif Footbalist.A >=11 and Footbalist.B < 11:
            Footbalist.B += 1
            return 'B'
        elif Footbalist.A < 11 and Footbalist.B >= 11:
            Footbalist.A += 1
            return 'A'



for i in range (0, len(List)):
    List [i] = Footbalist (List [i])
    print ('%s %s' % (List [i].name ,List [i]. Team ()))
  