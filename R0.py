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
        self.num =""
    
    def interp(self, _num = None):
        if(not _num):
            self.num = int(input("Read: "))
        else:
            self.num = _num
        return self.num


