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
        print("Test failed expected "+ str(_expected) + " got "+ str(_actual))
        return False
    
    def testRandom(self, _r):
        print(_r.pp() + " value: " +str(_r.interp()))
    
    def testOpt(self):
        testCompleted = 0
        for i in range(100):
            print("Test Number: " +str(i))
            p = randomR0(6)
            pprim = optimizer(p)
            print(p.pp())
            print(pprim.pp())
            if(p.interp() == pprim.interp()):
                print(True)
                testCompleted+=1
        print("Number of optimizer tests completed " + str(testCompleted))

num_5 = RNum(5)
num_6 = RNum(6)
num_3 = RNum(3)
num_16 = RNum(16)
num_add_6_5 = RAdd(num_6,num_5)
num_neg_6 = RNegate(num_6)
num_add_neg_6_num_6 = RAdd(num_neg_6, num_6)
num_add_num_0_num_3 = RAdd(num_add_neg_6_num_6,num_3)
num_add_num_3_num_0 = RAdd(num_add_num_0_num_3,num_add_neg_6_num_6)
read_1 = RRead()
pow_3 = Pow(num_3)
pow_5 = Pow(num_5)
pow_16 = Pow(num_16)

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
print(s.test(read_1.interp(),1))    
print(s.test(read_1.interp(),1))    

print(s.test(pow_3.pp(),"2^3"))
print(s.test(pow_3.interp(),8))
print(s.test(pow_5.pp(),"2^5"))
print(s.test(pow_5.interp(),32))
print(s.test(pow_16.pp(),"2^16"))
print(s.test(pow_16.interp(),65536))
print(s.test(Pow(RNum(4)).interp(),16 ))

#Random testing 
s.testRandom(randomR0(7))
s.testRandom(randomR0(6))
s.testRandom(randomR0(5))
s.testRandom(randomR0(4))
s.testRandom(randomR0(3))
s.testRandom(randomR0(2))
s.testRandom(randomR0(1))
s.testRandom(randomR0(0))

#Optimized Tests
print("\nOptimizer Exs")
print(optimizer(RNegate(RNegate(RNegate(RNegate(RNegate(RRead())))))).pp())
print(optimizer(RNegate(RNegate(RNegate(RNegate(RNegate(RNegate(RRead()))))))).pp())
print(optimizer(RNegate(RAdd(RNum(10),RAdd(RRead(),RNum(12))))).pp())
print(optimizer(RNegate(RNegate(RNum(975)))).pp())
print(optimizer(RAdd(RNum(22),RNum(23))).pp())
print(optimizer(RAdd(RNegate(RNum(22)),RNum(23))).pp())
print(optimizer(RAdd(RNum(22),RAdd(RNum(23),RRead()))).pp())
print(optimizer(RAdd(RNum(22),RAdd(RNum(23),RNum(20)))).pp())

s.testOpt()
s.endSuite()
