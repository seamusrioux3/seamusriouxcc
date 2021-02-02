import random
from datetime import datetime

class RNum:
    def __init__(self, _num):
        self.num = _num

    def pp(self):
        return str(self.num)

    def interp(self):
        return self.num

class RNegate:
    def __init__(self,_num):
        self.num = _num
    
    def pp(self):
        return "-(" + str(self.num.pp()) + ")"
    
    def interp(self):
        return -1*self.num.interp()

class RAdd:
    def __init__(self, _left, _right):
        self.left =_left
        self.right = _right
    
    def pp(self):
        return "(+ " + self.left.pp() +" " + self.right.pp() + ")"
    
    def interp(self):
        return self.left.interp() + self.right.interp() 


class RRead:
    def __init__(self):
        self.num = 0
    
    def pp(self):
        return " Read "

    def interp(self):
        inp = input("Read: ")
        if(inp == ""):
            self.num = 1
        else:
            self.num = int(inp)
        return self.num

class Pow:
    def __init__(self, _num):
        self.num = _num
    
    def pp(self):
        return "2^" + str(self.num.pp()) 
    
    def interp(self):
        if(self.num.interp() == 0):
            return 1
        else:
            return RAdd(Pow(RNum(self.num.interp()-1)),Pow(RNum(self.num.interp()-1))).interp()


def randomR0(n):
    random.seed(datetime.now())
    ret =0
    if(n == 0):
        ret = random.choice([RNum(random.randint(0, 1024)),RRead()])
    else:
        ret = random.choice([RAdd(randomR0(n-1),randomR0(n-1)),RNegate(randomR0(n-1))])
    return ret

def optimizer(n):
    if isinstance(n,RNum):
        return n
    elif isinstance(n,RRead):
        return n
    elif isinstance(n,RNegate):
        return not_opt(n.num)
    elif isinstance(n,RAdd):
        l = n.left
        r = n.right
        if(isinstance(l,RNum) and isinstance(r,RNum)):
            return RNum(l.interp() + r.interp())

        elif(isinstance(l,RNum) and isinstance(r,RAdd) and isinstance(r.left,RNum)):
            return RAdd(RNum(l.interp() + r.left.interp()),r.right)

        elif(isinstance(l,RAdd) and isinstance(r,RNum) and isinstance(r.right,RNum)):
            return RAdd(RNum(l.interp() + r.right.interp()),r.left)

        elif(isinstance(l, RAdd) and isinstance(l.left, RNum) and isinstance(r,RAdd) and isinstance(r.left, RNum)):
            return RAdd(RNum(l.left.interp() + r.left.interp()),RAdd(l.left,r.left))
        elif(not isinstance(l,RNum) and isinstance(r,RNum)):
            return RAdd(r,l)
        else:
            return RAdd(optimizer(l), optimizer(r))
            
def not_opt(e):
    if(isinstance (e,RNum)):
        return RNum(-1 * e.num)
    elif(isinstance(e,RNegate)):
        return optimizer(e.num)
    elif(isinstance(e,RAdd)):
        if(isinstance(e.left,RNum)):
            return optimizer(RAdd(not_opt(e.left), not_opt(optimizer(e.right))))
        else:
            return RNegate(optimizer(e))
    else:
        return RNegate(e)
    
        
