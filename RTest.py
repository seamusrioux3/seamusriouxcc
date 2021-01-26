from R0 import *

class Test:
    def __init__(self):
        print("Starting test suite: ")
        self.testPassed = 0
        self.totalTests = 0

    def endSuite(self):
        print(str(self.testPassed) + " tests passed out of " + str(self.totalTests))

    def test(self, _actual, _expected):
        self.totalTests +=1
        if(_actual == _expected):
            self.testPassed +=1
            return True
        print("Test failed expected: "+ str(_actual))
        return False

num_5 = RNum(5)
num_6 = RNum(6)
num_3 = RNum(3)
num_add_6_5 = RAdd(num_6,num_5)
num_neg_6 = RNegate(num_6)
num_add_neg_6_num_6 = RAdd(num_neg_6, num_6)
num_add_num_0_num_3 = RAdd(num_add_neg_6_num_6,num_3)
num_add_num_3_num_0 = RAdd(num_add_num_0_num_3,num_add_neg_6_num_6)
read_1 = RRead()

print(RNum(5).pp())
print(RNegate(RNum(5)).pp())
print(RAdd(RNum(5),RNum(6)).pp())
print(RAdd(RNegate(RNum(5)),RNum(6)).pp())
print(RAdd(RAdd(RNum(5),RNum(6)),RNum(6)).pp())

s = Test()

print(s.test(num_5.pp(), "5"))
print(s.test(num_6.pp(), "6"))
print(s.test(num_3.pp(), "3"))
print(s.test(num_add_6_5.pp(), "(+ 6 5)"))
print(s.test(num_neg_6.pp(), "-(6)"))
print(s.test(num_add_neg_6_num_6.pp(), "(+ -(6) 6)"))
print(s.test(num_add_num_0_num_3.pp(), "(+ (+ -(6) 6) 3)"))
print(s.test(num_add_num_3_num_0.pp(), "(+ (+ (+ -(6) 6) 3) (+ -(6) 6))"))

print(s.test(num_5.interp(), 5))
print(s.test(num_6.interp(), 6))
print(s.test(num_3.interp(), 3))
print(s.test(num_add_6_5.interp(), 11))
print(s.test(num_neg_6.interp(), -6))
print(s.test(num_add_neg_6_num_6.interp(), 0))
print(s.test(num_add_num_0_num_3.interp(), 3))
print(s.test(num_add_num_3_num_0.interp(), 3))
print(s.test(read_1.interp(),1))
print(s.test(read_1.interp(1),1))    
print(s.test(read_1.interp(),3))          
                     
s.endSuite()
