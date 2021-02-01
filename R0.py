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
        return str(self.num)

    def interp(self):
        inp = input("Read: ")
        if(inp == ""):
            self.num = self.num+1
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
