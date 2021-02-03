import random
from datetime import datetime

#R0 Data types
class RNum:
    def __init__(self, _num):
        self.num = _num

    def pp(self):
        return str(self.num)

    def interp(self, e = None):
        return self.num

class RNegate:
    def __init__(self,_num):
        self.num = _num
    
    def pp(self):
        return "-(" + str(self.num.pp()) + ")"
    
    def interp(self, e = None):
        if(e):
            return -1*self.num.interp(e)
        return -1*self.num.interp()

class RAdd:
    def __init__(self, _left, _right):
        self.left =_left
        self.right = _right
    
    def pp(self):
        return "(+ " + self.left.pp() +" " + self.right.pp() + ")"
    
    def interp(self, e = None):
        if(e):
            return self.left.interp(e) +  self.right.interp(e) 
        else:
            return self.left.interp() + self.right.interp() 
    

class RRead:
    def __init__(self):
        self.num = 0
    
    def pp(self):
        return "Read"

    def interp(self,  e = None):
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

#R1 data types
class RVar:
    def __init__(self, _name):
        self.name = _name
    
    def pp(self):
        return str(self.name)
    
    def interp(self, e = None):
        if(e[self.name]):
            return e[self.name].interp(e)
        return "ERROR"
    

class RLet:
    def __init__(self, _var, _l, _r):
        self.var = _var
        self.l = _l
        self.r = _r
    
    def pp(self):
        return "Let " + self.var.pp() +" = " + self.l.pp() +" in " + self.r.pp()
    
    def interp(self, e = None):
        if(e):
            e[self.var.name] = self.l
            return self.r.interp(e)
        else:
            env ={}
            env[self.var.name] = self.l
            return self.r.interp(env)



#Functions
def randomR0(n):
    random.seed(datetime.now())
    ret =0
    if(n == 0):
        ret = random.choice([RNum(random.randint(0, 16)),RRead()])
    else:
        ret = random.choice([RAdd(randomR0(n-1),randomR0(n-1)),RNegate(randomR0(n-1))])
    return ret

def randomR1(n,v):
    random.seed(datetime.now())
    ret =0
    if(n == 0):
        if(v):
            chosenVar = random.choice(v)
            ret = random.choice([RNum(random.randint(0, 16)), chosenVar , RRead()])
        else:
            ret = random.choice([RNum(random.randint(0, 16)), RRead()])
    else:
        newVar = RVar("V" + str(len(v)))
        ret = random.choice([RAdd(randomR1(n-1, v),randomR1(n-1, v)),RNegate(randomR1(n-1, v)), RLet(newVar,randomR1(n-1,v),randomR1(n-1,v+[newVar]))])
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
    
        
