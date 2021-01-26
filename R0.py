class RNum:
    def __init__(self, _num):
        self.num = _num

    def pp(self):
        return str(self.num)

class RNegate:
    def __init__(self,_num):
        self.num = _num
    
    def pp(self):
        return "-(" + str(self.num.pp()) + ")"

class RAdd:
    def __init__(self, _left, _right):
        self.left =_left
        self.right = _right
    
    def pp(self):
        return "(+ " + self.left.pp() +" " + self.right.pp() + ")"

class RRead:
    def __init__(self):
        print("Not implemented")

