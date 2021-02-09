from R0 import *


class Test:
    def __init__(self):
        print("Starting test suite: ")
        self.testPassed = 0
        self.totalTests = 0

    def endSuite(self):
        print(str(self.testPassed) + " tests passed out of " + str(self.totalTests))

    def test(self, _actual, _expected):
        self.totalTests += 1
        if(_actual == _expected):
            self.testPassed += 1
            return True
        print("Test failed expected " + str(_expected) + " got " + str(_actual))
        return False

    def testRandom(self, _r):
        print(_r.pp() + " value: \n" + str(_r.interp()))
        # print(_r.pp())

    def testOpt(self, n):
        testCompleted = 0
        for i in range(n):
            print("Test Number: " + str(i))
            p = randomR0(6)
            pprim = optimizer(p)
            print(p.pp())
            print(pprim.pp())
            if(p.interp() == pprim.interp()):
                print(True)
                testCompleted += 1
        print("Number of optimizer tests completed " +
              str(testCompleted) + " out of "+str(n))


num_5 = RNum(5)
num_6 = RNum(6)
num_3 = RNum(3)
num_16 = RNum(16)
num_add_6_5 = RAdd(num_6, num_5)
num_neg_6 = RNegate(num_6)
num_add_neg_6_num_6 = RAdd(num_neg_6, num_6)
num_add_num_0_num_3 = RAdd(num_add_neg_6_num_6, num_3)
num_add_num_3_num_0 = RAdd(num_add_num_0_num_3, num_add_neg_6_num_6)
read_1 = RRead()
pow_3 = Pow(num_3)
pow_5 = Pow(num_5)
pow_16 = Pow(num_16)

print(RNum(5).pp())
print(RNegate(RNum(5)).pp())
print(RAdd(RNum(5), RNum(6)).pp())
print(RAdd(RNegate(RNum(5)), RNum(6)).pp())
print(RAdd(RAdd(RNum(5), RNum(6)), RNum(6)).pp())

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

# print(s.test(read_1.interp(),1))
# print(s.test(read_1.interp(),1))
# print(s.test(read_1.interp(),1))

print(s.test(pow_3.pp(), "2^3"))
print(s.test(pow_3.interp(), 8))
print(s.test(pow_5.pp(), "2^5"))
print(s.test(pow_5.interp(), 32))
print(s.test(pow_16.pp(), "2^16"))
print(s.test(pow_16.interp(), 65536))
print(s.test(Pow(RNum(4)).interp(), 16))

# Random testing
# s.testRandom(randomR0(7))
# s.testRandom(randomR0(6))
# s.testRandom(randomR0(5))
# s.testRandom(randomR0(4))
# s.testRandom(randomR0(3))
# s.testRandom(randomR0(2))
# s.testRandom(randomR0(1))
# s.testRandom(randomR0(0))

# Optimized Tests
print("\nOptimizer Exs")
print(optimizer(RNegate(RNegate(RNegate(RNegate(RNegate(RRead())))))).pp())
print(optimizer(RNegate(RNegate(RNegate(RNegate(RNegate(RNegate(RRead()))))))).pp())
print(optimizer(RNegate(RAdd(RNum(10), RAdd(RRead(), RNum(12))))).pp())
print(optimizer(RNegate(RNegate(RNum(975)))).pp())
print(optimizer(RAdd(RNum(22), RNum(23))).pp())
print(optimizer(RAdd(RNegate(RNum(22)), RNum(23))).pp())
print(optimizer(RAdd(RNum(22), RAdd(RNum(23), RRead()))).pp())
print(optimizer(RAdd(RNum(22), RAdd(RNum(23), RNum(20)))).pp())
# s.testOpt(2)


# Variable and Let testing
print("\nR1 Tests")
letTest1 = RLet(RVar("x"), RNum(2), RAdd(RVar("x"), RNum(3)))
letTest2 = RLet(RVar("x"), RNum(2), RLet(
    RVar("y"), RNum(1), RAdd(RVar("x"), RVar("y"))))
letTest3 = RLet(RVar("x"), RNum(2), RLet(
    RVar("x"), RNum(1), RAdd(RVar("x"), RVar("x"))))
letTest4 = RLet(RVar("x"), RNum(3), RLet(RVar("y"), RNum(2), RLet(
    RVar("z"), RNum(1), RAdd(RVar("x"), RAdd(RVar("y"), RVar("z"))))))
letTest5 = RLet(RVar("x"), RRead(), RAdd(RVar("x"), RVar("x")))
letTest6 = RLet(RVar("x"), RNum(3), RNegate(RVar("x")))
letTest7 = RLet(RVar("x"), RNum(7), RLet(RVar("y"), RNum(8),
                                         RAdd(RNegate(RVar("x")), RNegate(RVar("y")))))
letTest8 = RLet(RVar("x"), RNum(7), RLet(RVar("x"), RNum(8),
                                         RAdd(RNegate(RVar("x")), RNegate(RVar("x")))))
letTest9 = RLet(RVar("x"), RRead(), RNum(4))
# print(letTest1.pp() + " evals to: " + str(letTest1.interp()))
# print(letTest2.pp() + " evals to: " + str(letTest2.interp()))
# print(letTest3.pp() + " evals to: " + str(letTest3.interp()))
# print(letTest4.pp() + " evals to: " + str(letTest4.interp()))
# print(letTest5.pp() + " evals to: " + str(letTest5.interp()))
# print(letTest6.pp() + " evals to: " + str(letTest6.interp()))
# print(letTest7.pp() + " evals to: " + str(letTest7.interp()))
# print(letTest8.pp() + " evals to: " + str(letTest8.interp()))
print(letTest9.pp() + " evals to: " + str(letTest9.interp()))

############# randomR1 Testing #################
print("\nRandomR1 Tests")
# s.testRandom(randomR1(0,[]))
# s.testRandom(randomR1(1,[]))
# s.testRandom(randomR1(2,[]))
# s.testRandom(randomR1(3,[]))
# s.testRandom(randomR1(4,[]))
# s.testRandom(randomR1(5,[]))
# s.testRandom(randomR1(6,[]))
# s.testRandom(randomR1(7,[]))
# s.testRandom(randomR1(8,[]))

########### Optimizer Testing R1 ###############
print("\nOptimizerR1 Tests")
letTest1Opt = optimizer(letTest1)
letTest2Opt = optimizer(letTest2)
letTest3Opt = optimizer(letTest3)
letTest4Opt = optimizer(letTest4)
letTest5Opt = optimizer(letTest5)
letTest6Opt = optimizer(letTest6)
letTest7Opt = optimizer(letTest7)
letTest8Opt = optimizer(letTest8)

print("test1")
print(letTest1.pp() + " --> " + letTest1Opt.pp())
print(str(letTest1.interp()) + " --> " + str(letTest1Opt.interp()))

print("test2")
print(letTest2.pp() + " --> " + letTest2Opt.pp())
print(str(letTest2.interp()) + " --> " + str(letTest2Opt.interp()))

print("test3")
print(letTest3.pp() + " --> " + letTest3Opt.pp())
print(str(letTest3.interp()) + " --> " + str(letTest3Opt.interp()))

print("test4")
print(letTest4.pp() + " --> " + letTest4Opt.pp())
print(str(letTest4.interp()) + " --> " + str(letTest4Opt.interp()))

# print("test5")
# print(letTest5.pp() + " --> " + letTest5Opt.pp() )
# print(str(letTest5.interp()) +" --> " + str(letTest5Opt.interp()))

# print("test6")
# print(letTest6.pp() + " --> " + letTest6Opt.pp() )
# print(str(letTest6.interp()) +" --> " + str(letTest6Opt.interp()))

# print("test7")
# print(letTest7.pp() + " --> " + letTest7Opt.pp() )
# print(str(letTest7.interp()) +" --> " + str(letTest7Opt.interp()))

# print("test8")
# print(letTest8.pp() + " --> " + letTest8Opt.pp() )
# print(str(letTest8.interp()) +" --> " + str(letTest8Opt.interp()))


########## X0 Program Testing ################
Xprog1 = XProgram([
    (XLabel("main"),
     XBlock([
         XIMov(XCon(10), XRegister("R8")),
         XIMov(XCon(5), XRegister("R9")),
         XIJmp(XLabel("l0"))
     ])),
    (XLabel("l0"),
     XBlock([
         XIAdd(XRegister("R8"), XRegister("R9")),
         XIAdd(XRegister("R8"), XRegister("R9")),
         XIMov(XRegister("R9"), XRegister("RAX")),
         XIRet()
     ])),
])

Xprog2 = XProgram([
    (XLabel("main"),
     XBlock([XIMov(XCon(10), XRegister("R8")),
             XIMov(XCon(5), XRegister("R9")),
             XIJmp(XLabel("l0"))])),
    (XLabel("l0"),
     XBlock([
         XISub(XRegister("R8"), XRegister("R9")),
         XIAdd(XRegister("R8"), XRegister("R9")),
         XIMov(XRegister("R9"), XRegister("RAX")),
         XIRet()
     ])),
])

Xprog3 = XProgram([(
    XLabel("main"),
    XBlock([XIMov(XCon(10), XRegister("R8")),
            XIMov(XCon(5), XRegister("RAX")),
            XIRet()
            ])
)])

Xprog4 = XProgram([
    (
        XLabel("l0"),
        XBlock([
            XIMov(XCon(250), XRegister("RAX")),
            XIRet()
        ])
    ),
    (
        XLabel("main"),
        XBlock([
            XIMov(XCon(200), XRegister("RAX")),
            XIJmp(XLabel("l0"))
        ])),
])

Xprog5 = XProgram([
    (
        XLabel("l0"),
        XBlock([
            XISub(XRegister("R10"), XRegister("R8")),
            XIMov(XRegister("R10"), XRegister("RAX")),
            XIRet()
        ])
    ),
    (
        XLabel("main"),
        XBlock([
            XIMov(XCon(200), XRegister("R8")),
            XIMov(XCon(201), XRegister("R10")),
            XIJmp(XLabel("l0"))
        ])),
])

Xprog6 = XProgram([
    (
        XLabel("l0"),
        XBlock([
            XISub(XRegister("R10"), XRegister("R8")),
            XINeg(XRegister("R10")),
            XIMov(XRegister("R10"), XRegister("RAX")),
            XIRet()
        ])
    ),
    (
        XLabel("main"),
        XBlock([
            XIMov(XCon(200), XRegister("R8")),
            XIMov(XCon(201), XRegister("R10")),
            XIJmp(XLabel("l0"))
        ])),
])

Xprog7 = XProgram(
    [(
        XLabel("main"),
        XBlock([
            XIMov(XCon(8), XRegister("RAX")),
            XIMov(XCon(10), XRegister("RBX")),
            XIAdd(XRegister("RAX"), XRegister("RBX")),
            XIRet(),
        ])
    )]
)

Xprog8 = XProgram(
    [
        (
            XLabel("main"),
            XBlock([
                XIPush(XCon(33)),
                XIPop(XRegister("RAX")),
                XIRet()
            ])
        )
    ]
)

Xprog9 = XProgram(
    [
        (
            XLabel("main"),
            XBlock([
                XIMov(XCon(0), XRegister("R8")),
                XICall(XLabel("read_int")),
                XIAdd(XRegister("RAX"), XRegister("R8")),
                XICall(XLabel("read_int")),
                XIAdd(XRegister("RAX"), XRegister("R8")),
                XICall(XLabel("read_int")),
                XIAdd(XRegister("RAX"), XRegister("R8")),
                XIMov(XRegister("R8"), XRegister("RAX")),
                XIRet(),
            ])
        )
    ]
)



s.endSuite()
