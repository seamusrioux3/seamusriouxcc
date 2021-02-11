from R0 import *
import subprocess
import os


class Test:
    def __init__(self):
        print("Starting test suite: ")
        self.testPassed = 0
        self.totalTests = 0

    def endSuite(self):
        print("\n" + str(self.testPassed) + " tests passed out of " + str(self.totalTests))

    def test(self, _actual, _expected):
        self.totalTests += 1
        if(_actual == _expected):
            print("Test passed got actual: "+ str(_actual) +" and expected: "+ str(_expected))
            self.testPassed += 1
            return True
        print("Test failed expected " + str(_expected) + " got " + str(_actual))
        return False

    def testRandom(self, _r):
        print(_r.pp() + " value: \n" + str(_r.interp()))

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
    
    def testX0Programs(self,prog):
        fileName = "c0.s"
        binName = "c0.bin"
        f = open(fileName, "w")
        f.write(prog.emit()+"\n")
        f.close()

        p = subprocess.Popen(

            ["cc",fileName,"runtime.c","-o","c0.bin"],

            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        
        stdout, stderr = p.communicate()
        exit_code = p.wait()

        p = subprocess.Popen(

            ["./" + binName],

            stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        stdout, stderr = p.communicate()
        exit_code = p.wait()

        if os.path.exists(binName):
            os.remove(binName)

        self.test(prog.interp(),exit_code)
    
    def testUniquify(self,p):
        actual = uniquify(p).interp()
        expected = p.interp()
        self.test(actual,expected)

    def testRCO(self,p):
        actual = RCO(p).interp()
        expected = p.interp()
        self.test(actual,expected)

    def testAll(self,p):
        actual = 0
        po = optimizer(p)
        pu = uniquify(po)
        pr = RCO(pu)
        if (p.interp() == po.interp() == pu.interp() == pr.interp()):
            actual = pr.interp()
        else:
            actual = False

        self.test(actual,p.interp())
    
   

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

s.test(num_5.pp(), "5")
s.test(num_6.pp(), "6")
s.test(num_3.pp(), "3")
s.test(num_add_6_5.pp(), "(+ 6 5)")
s.test(num_neg_6.pp(), "-(6)")
s.test(num_add_neg_6_num_6.pp(), "(+ -(6) 6)")
s.test(num_add_num_0_num_3.pp(), "(+ (+ -(6) 6) 3)")
s.test(num_add_num_3_num_0.pp(), "(+ (+ (+ -(6) 6) 3) (+ -(6) 6))")

s.test(num_5.interp(), 5)
s.test(num_6.interp(), 6)
s.test(num_3.interp(), 3)
s.test(num_add_6_5.interp(), 11)
s.test(num_neg_6.interp(), -6)
s.test(num_add_neg_6_num_6.interp(), 0)
s.test(num_add_num_0_num_3.interp(), 3)
s.test(num_add_num_3_num_0.interp(), 3)
s.test(pow_3.pp(), "2^3")
s.test(pow_3.interp(), 8)
s.test(pow_5.pp(), "2^5")
s.test(pow_5.interp(), 32)
s.test(pow_16.pp(), "2^16")
s.test(pow_16.interp(), 65536)
s.test(Pow(RNum(4)).interp(), 16)

# Random testing
print("\nRandom R0 Testing\n")
s.testRandom(randomR0(7))
s.testRandom(randomR0(6))
s.testRandom(randomR0(5))
s.testRandom(randomR0(4))
s.testRandom(randomR0(3))
s.testRandom(randomR0(2))
s.testRandom(randomR0(1))
s.testRandom(randomR0(0))

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


############# randomR1 Testing #################
print("\nRandomR1 Tests")
s.testRandom(randomR1(0,[]))
s.testRandom(randomR1(1,[]))
s.testRandom(randomR1(2,[]))
s.testRandom(randomR1(3,[]))
s.testRandom(randomR1(4,[]))
s.testRandom(randomR1(5,[]))
s.testRandom(randomR1(6,[]))
s.testRandom(randomR1(7,[]))
s.testRandom(randomR1(8,[]))

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

Xprog10 = XProgram(
    [
        (
            XLabel("main"),
            XBlock([
                XIPush(XCon(33)),
                XIPop(XRegister("RAX")),
                XIPush(XCon(66)),
                XIPop(XRegister("RAX")),
                XIPush(XCon(99)),
                XIPop(XRegister("RAX")),
                XIRet()
            ])
        )
    ]
)

Xprog11 = XProgram(
    [
        (
            XLabel("main"),
            XBlock([
                XIPush(XCon(33)),
                XIPop(XRegister("RAX")),
                XIMov(XCon(8),XRegister("R8")),
                XIAdd(XRegister("R8"),XRegister("RAX")),
                XIRet()
            ])
        )
    ]
)

s.testX0Programs(Xprog1)
s.testX0Programs(Xprog2)
s.testX0Programs(Xprog3)
s.testX0Programs(Xprog4)
s.testX0Programs(Xprog5)
s.testX0Programs(Xprog6)
s.testX0Programs(Xprog7)
s.testX0Programs(Xprog8)
s.testX0Programs(Xprog9)
s.testX0Programs(Xprog10)
s.testX0Programs(Xprog11)


##### Testing C0 Programs ######
Cprog1 = CProgram({
    CLabel("main"):
    [
        CSet(CVar("i"),CNum(10)),
        CSet(CVar("j"),CNum(5)),
        CSet(CVar("k"),CAdd(CVar("i"),CVar("j"))),
        CSet(CVar("l"),CAdd(CVar("i"),CVar("k"))),
        CRet(CVar("l"))
    ]
})
print(Cprog1.pp()+"\n")
s.test(Cprog1.interp(),25)

Cprog2 = CProgram({
    CLabel("main"):
    [
        CSet(CVar("1"), CRead()),
        CSet(CVar("2"), CRead()),
        CSet(CVar("3"), CRead()),
        CSet(CVar("4"), CAdd(CVar("1"),CVar("2"))),
        CSet(CVar("5"), CAdd(CVar("3"),CVar("4"))),
        CRet(CVar("5"))
    ]
})

print(Cprog2.pp()+"\n")
s.test(Cprog2.interp(),6)


Cprog3 = CProgram({
    CLabel("main"):
    [
        CSet(CVar("8"), CNum(10)),
        CSet(CVar("9"), CNum(5)),
        CSet(CVar("10"), CNeg(CVar("8"))),
        CSet(CVar("11"), CAdd(CVar("10"), CVar("9"))),
        CSet(CVar("12"), CAdd(CVar("8"),  CVar("11"))),
        CRet(CVar("12"))
    ]
})

print(Cprog3.pp()+"\n")
s.test(Cprog3.interp(),5)

Cprog4 = CProgram({
    CLabel("main"):
    [
        CSet(CVar("0"), CNum(10)),
        CSet(CVar("1"), CNum(5)),
        CRet(CVar("1"))
    ]
})

print(Cprog4.pp()+"\n")
s.test(Cprog4.interp(),5)

Cprog5 = CProgram({
    CLabel("main"):
    [
        CSet(CVar("0"), CNum(200)),
        CSet(CVar("0"), CNum(250)),
        CRet(CVar("0")),
    ]
})

print(Cprog5.pp()+"\n")
s.test(Cprog5.interp(),250)

Cprog6 = CProgram({
    CLabel("main"):
    [
        CSet(CVar("8"),  CNum(200)),
        CSet(CVar("10"), CNum(201)),
        CSet(CVar("11"), CAdd(CNeg(CVar("10")), CVar("8"))),
        CSet(CVar("12"), CVar("10")),
        CRet(CVar("10"))
    ]
})

print(Cprog6.pp()+"\n")
s.test(Cprog6.interp(),201)

Cprog7 = CProgram({
    CLabel("main"):
    [
        CSet(CVar("A"), CNum(8)),
        CSet(CVar("B"), CNum(10)),
        CSet(CVar("C"), CAdd(CVar("A"), CVar("B"))),
        CRet(CVar("C"))
    ]
})

print(Cprog7.pp()+"\n")
s.test(Cprog7.interp(),18)

####### Uniquify Tests ###########
print("\n Uniquify Tests\n")
Uprog1 = RLet(RVar("A"), RNum(1),RLet(RVar("A"),RRead(),RVar("A")))
Uprog2 = RLet(RVar("A"), RNum(1), RLet(RVar("A"),RNum(2),RAdd(RVar("A"),RVar("A"))))
Uprog3 = RLet(RVar("A"), RNum(1), RVar("A"))
Uprog4 = RLet(RVar("A"), RNegate(RLet(RVar("A"),RNum(2),RAdd(RVar("A"),RVar("A")))), RAdd(RVar("A"),RVar("A")))
Uprog5 = RAdd(RLet(RVar("x"), RNum(7), RVar("x")), RLet(RVar("x"), RNum(8), RLet(RVar("x"),RAdd(RNum(1),RVar("x")), RAdd(RVar("x"), RVar("x")))))
Uprog6 = RLet(RVar("A"), RLet(RVar("A"), RLet(RVar("A"), RNum(2), RAdd(RVar("A"),RVar("A"))), RAdd(RVar("A"), RVar("A"))), RAdd(RVar("A"), RVar("A")))

s.testUniquify(Uprog1)
s.testUniquify(Uprog2)
s.testUniquify(Uprog3)
s.testUniquify(Uprog4)
s.testUniquify(Uprog5)
s.testUniquify(Uprog6)
s.testUniquify(randomR1(5,[]))
s.testUniquify(randomR1(4,[]))
s.testUniquify(randomR1(3,[]))

####### RCO Tests ###########
print("\nRCO Tests\n")
Rcoprog1 = RAdd(RAdd(RNum(2), RNum(3)), RLet(RVar("x"), RRead(), RAdd(RVar("x"), RVar("x"))))
Rcoprog2 = RLet(RVar("R1"), RAdd(RNum(2), RNum(3)), RLet(RVar("R2"), RAdd(RNum(1), RVar("R1")), RLet(RVar("R3"), RAdd(RVar("R1"), RVar("R1")), RVar("R2"))))
Rcoprog3 = RLet(RVar("R1"), RNegate(RNum(3)), RLet(RVar("R2"), RAdd(RNum(1), RVar("R1")), RLet(RVar("R3"), RAdd(RVar("R1"), RVar("R1")), RVar("R2"))))
Rcoprog4 = RCO(optimizer(RAdd(RAdd(RNum(2), RNum(3)), RLet(RVar("x"), RRead(), RAdd(RVar("x"), RVar("x"))))))
Rcoprog5 = RLet(RVar("R1"), RAdd(RNum(1), RNum(1)), RLet(RVar("R2"), RAdd(RVar("R1"), RVar("R1")), RLet(RVar("R3"),RAdd(RVar("R2"),RVar("R2")), RVar("R3"))))
Rcoprog6 = RLet(RVar("R1"), RAdd(RNegate(RNum(2)), RNegate(RNegate(RNum(2)))), RVar("R1"))

s.testRCO(Rcoprog1)
s.testRCO(Rcoprog2)
s.testRCO(Rcoprog3)
s.testRCO(Rcoprog4)
s.testRCO(Rcoprog5)
s.testRCO(Rcoprog6)


####### Combined Testing ########
print("\nCombined Tests\n")
s.testAll(letTest1)
s.testAll(letTest2)
s.testAll(letTest3)
s.testAll(letTest4)
s.testAll(letTest5)
s.testAll(letTest6)
s.testAll(letTest7)
s.testAll(letTest8)
s.testAll(letTest9)

s.endSuite()
