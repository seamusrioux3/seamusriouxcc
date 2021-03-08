from R0 import *
import subprocess
import os


class Test:
    def __init__(self):
        print("Starting test suite: ")
        self.testPassed = 0
        self.totalTests = 0

    def endSuite(self):
        print("\n" + str(self.testPassed) +
              " tests passed out of " + str(self.totalTests))

    def test(self, _actual, _expected):
        self.totalTests += 1
        if(_actual == _expected):
            print("Test passed got actual: " + str(_actual) +
                  " and expected: " + str(_expected))
            self.testPassed += 1
            return True
        print("Test failed expected " + str(_expected) + " got " + str(_actual))
        exit(1)
        return False

    def testX0OnHardware(self, prog):
        fileName = "c0.s"
        binName = "c0.bin"
        f = open(fileName, "w")
        f.write(prog.emit()+"\n")
        f.close()

        p = subprocess.Popen(

            ["cc", fileName, "runtime.c", "-o", "c0.bin"],

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

        return int(stdout)

    def getToXP(self, r):
        pu = uniquify(r)
        prco = RCO(pu)
        pecon = econ(prco)
        xp = select(pecon)
        uncl = uncover_live(xp)
        built = buildInt(uncl)
        aloc = allocate_registers(built)
        ptch = patch(aloc)
        return ptch

    def checkAll(self, org: RLet, arr, real: int):
        for a in arr:
            if(not org.interp() == a.interp()):
                return False
        if(real and not real == org.interp()):
            return False
        return True

    def testAll(self, p):
        actual = 0
        po = optimizer(p)
        pu = uniquify(p)
        pr = RCO(pu)
        pe = econ(pr)
        xz = select(pe)
        uncl = uncover_live(xz)
        built = buildInt(uncl)
        aloc = allocate_registers(built)
        ptch = patch(aloc)
        real = self.testX0OnHardware(ptch)

        # print("optimized: " + po.pp())
        # print("uniquify: " + pu.pp())
        # print("rco: " + pr.pp())
        # print("econ: " + pe.pp())
        # print("sel: " + xz.emit())

        # print("original: " + p.pp())

        # print("original ans: " + str(p.interp()))
        # print("optimized ans: " + str(po.interp()))
        # print("uniquify ans: " + str(pu.interp()))
        # print("rco ans: " + str(pr.interp()))
        # print("econ ans: " + str(pe.interp()))
        # print("sel ans: " + str(xz.interp()))
        # print("aloc ans: " + str(aloc.interp()))
        # print("patch ans: " + str(ptch.interp()))
        # print("real ans: " + str(real))
        if (self.checkAll(p, [pu, po, pr, pe, xz, uncl, built, aloc, ptch], real)):
            print(ptch.emit())
            actual = ptch.interp()  # aloc.interp()
        else:
            print("patch: " + ptch.emit())
            print("original ans: " + str(p.interp()))
            print("optimized ans: " + str(po.interp()))
            print("uniquify ans: " + str(pu.interp()))
            print("rco ans: " + str(pr.interp()))
            print("econ ans: " + str(pe.interp()))
            print("sel ans: " + str(xz.interp()))
            print("aloc ans: " + str(aloc.interp()))
            print("patch ans: " + str(ptch.interp()))
            print("real ans: " + str(real))
            actual = not p.interp()
            # exit(1)

        self.test(actual, p.interp())


s = Test()
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

letTest10 = RLet(RVar("x"), RRead(), RLet(RVar("y"), RRead(),
                                          RAdd(RAdd(RVar("x"), RVar("y")), RNum(42))))

########## X0 Program Testing ################
Xprog1 = XProgram([], {
    XLabel("main"):
    [
        XIMov(XCon(10), XRegister("R8")),
        XIMov(XCon(5), XRegister("R9")),
        XIJmp(XLabel("l0"))
    ],
    XLabel("l0"):
    [
        XIAdd(XRegister("R8"), XRegister("R9")),
        XIAdd(XRegister("R8"), XRegister("R9")),
        XIMov(XRegister("R9"), XRegister("RAX")),
        XIRet()
    ],
})

Xprog2 = XProgram([], {
    XLabel("main"):
    [
        XIMov(XCon(10), XRegister("R8")),
        XIMov(XCon(5), XRegister("R9")),
        XIJmp(XLabel("l0"))
    ],
    XLabel("l0"):
    [
        XISub(XRegister("R8"), XRegister("R9")),
        XIAdd(XRegister("R8"), XRegister("R9")),
        XIMov(XRegister("R9"), XRegister("RAX")),
        XIRet()
    ],
})

Xprog3 = XProgram([], {
    XLabel("main"):
    [
        XIMov(XCon(10), XRegister("R8")),
        XIMov(XCon(5), XRegister("RAX")),
        XIRet()
    ]
})

Xprog4 = XProgram([], {
    XLabel("l0"):
    [
        XIMov(XCon(250), XRegister("RAX")),
        XIRet()
    ],
    XLabel("main"):
    [
        XIMov(XCon(200), XRegister("RAX")),
        XIJmp(XLabel("l0"))
    ]
})

Xprog5 = XProgram([], {
    XLabel("l0"):
    [
        XISub(XRegister("R10"), XRegister("R8")),
        XIMov(XRegister("R10"), XRegister("RAX")),
        XIRet()
    ],
    XLabel("main"):
    [
        XIMov(XCon(200), XRegister("R8")),
        XIMov(XCon(201), XRegister("R10")),
        XIJmp(XLabel("l0"))
    ]
})

Xprog6 = XProgram([], {
    XLabel("l0"):
    [
        XISub(XRegister("R10"), XRegister("R8")),
        XIMov(XRegister("R10"), XRegister("RAX")),
        XIRet()
    ],
    XLabel("main"):
    [
        XIMov(XCon(200), XRegister("R8")),
        XIMov(XCon(201), XRegister("R10")),
        XIJmp(XLabel("l0"))
    ],
})

Xprog7 = XProgram([], {
    XLabel("main"):
    [
        XIMov(XCon(8), XRegister("RAX")),
        XIMov(XCon(10), XRegister("RBX")),
        XIAdd(XRegister("RAX"), XRegister("RBX")),
        XIRet(),
    ]
})

Xprog8 = XProgram([], {
    XLabel("main"):
    [
        XIPush(XCon(33)),
        XIPop(XRegister("RAX")),
        XIRet()
    ]
})

Xprog9 = XProgram([], {
    XLabel("main"):
    [
        XIMov(XCon(0), XRegister("R8")),
        XICall(XLabel("read_int")),
        XIAdd(XRegister("RAX"), XRegister("R8")),
        XICall(XLabel("read_int")),
        XIAdd(XRegister("RAX"), XRegister("R8")),
        XICall(XLabel("read_int")),
        XIAdd(XRegister("RAX"), XRegister("R8")),
        XIMov(XRegister("R8"), XRegister("RAX")),
        XIRet(),
    ]
})

Xprog10 = XProgram([], {
    XLabel("main"): [
        XIPush(XCon(33)),
        XIPop(XRegister("RAX")),
        XIPush(XCon(66)),
        XIPop(XRegister("RAX")),
        XIPush(XCon(99)),
        XIPop(XRegister("RAX")),
        XIRet()
    ]
})

Xprog11 = XProgram([], {
    XLabel("main"):
    [
        XIPush(XCon(33)),
        XIPop(XRegister("RAX")),
        XIMov(XCon(8), XRegister("R8")),
        XIAdd(XRegister("R8"), XRegister("RAX")),
        XIRet()
    ]
})
##### Testing C0 Programs ######

Cprog2 = CProgram([], {
    CLabel("main"):
    [
        CSet(CVar("1"), CRead()),
        CSet(CVar("2"), CRead()),
        CSet(CVar("3"), CRead()),
        CSet(CVar("4"), CAdd(CVar("1"), CVar("2"))),
        CSet(CVar("5"), CAdd(CVar("3"), CVar("4"))),
        CRet(CVar("5"))
    ]
})

Cprog3 = CProgram([], {
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

Cprog4 = CProgram([], {
    CLabel("main"):
    [
        CSet(CVar("0"), CNum(10)),
        CSet(CVar("1"), CNum(5)),
        CRet(CVar("1"))
    ]
})

Cprog5 = CProgram([], {
    CLabel("main"):
    [
        CSet(CVar("0"), CNum(200)),
        CSet(CVar("0"), CNum(250)),
        CRet(CVar("0")),
    ]
})
Cprog6 = CProgram([], {
    CLabel("main"):
    [
        CSet(CVar("8"),  CNum(200)),
        CSet(CVar("10"), CNum(201)),
        CSet(CVar("11"), CAdd(CNeg(CVar("10")), CVar("8"))),
        CSet(CVar("12"), CVar("10")),
        CRet(CVar("10"))
    ]
})
Cprog7 = CProgram([], {
    CLabel("main"):
    [
        CSet(CVar("A"), CNum(8)),
        CSet(CVar("B"), CNum(10)),
        CSet(CVar("C"), CAdd(CVar("A"), CVar("B"))),
        CRet(CVar("C"))
    ]
})
# ####### Uniquify Tests ###########
print("\n Uniquify Tests\n")
Uprog1 = RLet(RVar("A"), RNum(1), RLet(RVar("A"), RRead(), RVar("A")))
Uprog2 = RLet(RVar("A"), RNum(1), RLet(
    RVar("A"), RNum(2), RAdd(RVar("A"), RVar("A"))))
Uprog3 = RLet(RVar("A"), RNum(1), RVar("A"))
Uprog4 = RLet(RVar("A"), RNegate(RLet(RVar("A"), RNum(2), RAdd(
    RVar("A"), RVar("A")))), RAdd(RVar("A"), RVar("A")))
Uprog5 = RAdd(RLet(RVar("x"), RNum(7), RVar("x")), RLet(RVar("x"), RNum(
    8), RLet(RVar("x"), RAdd(RNum(1), RVar("x")), RAdd(RVar("x"), RVar("x")))))
Uprog6 = RLet(RVar("A"), RLet(RVar("A"), RLet(RVar("A"), RNum(2), RAdd(
    RVar("A"), RVar("A"))), RAdd(RVar("A"), RVar("A"))), RAdd(RVar("A"), RVar("A")))

# ####### RCO Tests ###########
print("\nRCO Tests\n")
Rcoprog1 = RAdd(RAdd(RNum(2), RNum(3)), RLet(
    RVar("x"), RRead(), RAdd(RVar("x"), RVar("x"))))
Rcoprog2 = RLet(RVar("R1"), RAdd(RNum(2), RNum(3)), RLet(RVar("R2"), RAdd(RNum(
    1), RVar("R1")), RLet(RVar("R3"), RAdd(RVar("R1"), RVar("R1")), RVar("R2"))))
Rcoprog3 = RLet(RVar("R1"), RNegate(RNum(3)), RLet(RVar("R2"), RAdd(RNum(
    1), RVar("R1")), RLet(RVar("R3"), RAdd(RVar("R1"), RVar("R1")), RVar("R2"))))
Rcoprog4 = RCO(optimizer(RAdd(RAdd(RNum(2), RNum(3)), RLet(
    RVar("x"), RRead(), RAdd(RVar("x"), RVar("x"))))))
Rcoprog5 = RLet(RVar("R1"), RAdd(RNum(1), RNum(1)), RLet(RVar("R2"), RAdd(RVar(
    "R1"), RVar("R1")), RLet(RVar("R3"), RAdd(RVar("R2"), RVar("R2")), RVar("R3"))))
Rcoprog6 = RLet(RVar("R1"), RAdd(RNegate(RNum(2)),
                                 RNegate(RNegate(RNum(2)))), RVar("R1"))
Rcoprog7 = RLet(RVar("R1"), RNum(4), RVar("R1"))

# ####### Econ Examples ###########
Econprog1R = RLet(RVar("x"), RNum(2), RAdd(RVar("x"), RNum(3)))
Econprog1C = CProgram({
    CLabel("main"):
    [
        CSet(CVar("R1"), CAdd(CNum(2), CNum(3))),
        CRet(CVar("R1")),
    ]
})
Econprog2R = RLet(RVar("R1"), RAdd(RNum(2), RNum(3)), RLet(RVar("R2"), RAdd(
    RNum(1), RVar("R1")), RLet(RVar("R3"), RAdd(RVar("R1"), RVar("R1")), RVar("R3"))))

Econprog2C = CProgram({
    CLabel("main"):
    [
        CSet(CVar("R1"), CAdd(CNum(2), CNum(3))),
        CSet(CVar("R2"), CAdd(CNum(1), CVar("R1"))),
        CSet(CVar("R3"), CAdd(CVar("R1"), CVar("R1"))),
        CRet(CVar("R3")),
    ]
})
Econprog3R = RLet(RVar("R1"), RNegate(RNum(3)), RLet(RVar("R2"), RAdd(RNum(
    1), RVar("R1")), RLet(RVar("R3"), RAdd(RVar("R1"), RVar("R1")), RVar("R3"))))
Econprog3C = CProgram({
    CLabel("main"):
    [
        CSet(CVar("R1"), CNeg(CNum(3))),
        CSet(CVar("R2"), CAdd(CNum(1), CVar("R1"))),
        CSet(CVar("R3"), CAdd(CVar("R1"), CVar("R1"))),
        CRet(CVar("R3")),
    ]
})
Econprog4R = RLet(RVar("R1"), RAdd(RNum(1), RNum(1)), RLet(RVar("R2"), RAdd(RVar(
    "R1"), RVar("R1")), RLet(RVar("R3"), RAdd(RVar("R2"), RVar("R2")), RVar("R3"))))
Econprog4C = CProgram({
    CLabel("main"):
    [
        CSet(CVar("R1"), CAdd(CNum(1), CNum(1))),
        CSet(CVar("R2"), CAdd(CVar("R1"), CVar("R1"))),
        CSet(CVar("R3"), CAdd(CVar("R2"), CVar("R2"))),
        CRet(CVar("R3")),
    ]
})

Econprog5R = RLet(RVar("R1"), RAdd(RNegate(RNum(2)),
                                   RNegate(RNegate(RNum(2)))), RVar("R1"))
Econprog5C = CProgram({
    CLabel("main"):
    [
        CSet(CVar("R1"), CNeg(CNum(2))),
        CSet(CVar("R2"), CNeg(CNum(2))),
        CSet(CVar("R3"), CNeg(CVar("R2"))),
        CSet(CVar("R4"), CAdd(CVar("R1"), CVar("R3"))),
        CRet(CVar("R4")),
    ]
})
Econprog6R = RLet(RVar("R1"), RNum(4), RVar("R1"))
Econprog6C = CProgram({
    CLabel("main"):
    [
        CSet(CVar("R1"), CNum(4)),
        CRet(CVar("R1")),
    ]
})


########### R2 Programs Testing ##############
rTrue = RBool(True)
rFalse = RBool(False)
r2prog1 = RAnd(rTrue, rFalse)
r2prog2 = RAnd(rFalse, rFalse)
r2prog3 = ROr(rFalse, rTrue)
r2prog4 = RNot(rTrue)
r2prog5 = RCmp("<=", RNum(1), RNum(2))
r2prog6 = RCmp(">=", RNum(3), RNum(4))
r2prog7 = RCmp("<", RNum(5), RNum(6))
r2prog8 = RCmp("==", RNum(7), RNum(8))
r2prog9 = RCmp("==", RNum(9), RNum(9))
r2prog10 = RSub(RNum(10), RNum(10))
r2prog11 = RSub(RNum(20), RNum(10))
r2prog12 = RIf(r2prog5, RNum(5), RNum(2))
r2prog13 = RIf(r2prog6, RAdd(RNum(5), RNum(1)), RNum(2))
r2prog14 = RLet(RVar("v"), RNum(10), RLet(RVar("y"), RNum(10), RIf(
    RCmp("==", RVar("v"), RVar("y")), RVar("v"), RVar("y"))))

print(rTrue.pp())
print(rFalse.pp())
print(r2prog1.pp())
print(r2prog2.pp())
print(r2prog3.pp())
print(r2prog4.pp())
print(r2prog5.pp())
print(r2prog6.pp())
print(r2prog7.pp())
print(r2prog8.pp())
print(r2prog9.pp())
print(r2prog10.pp())
print(r2prog11.pp())
print(r2prog12.pp())
print(r2prog13.pp())
print(r2prog14.pp())

print(rTrue.interp())
print(rFalse.interp())
print(r2prog1.interp())
print(r2prog2.interp())
print(r2prog3.interp())
print(r2prog4.interp())
print(r2prog5.interp())
print(r2prog6.interp())
print(r2prog7.interp())
print(r2prog8.interp())
print(r2prog9.interp())
print(r2prog10.interp())
print(r2prog11.interp())
print(r2prog12.interp())
print(r2prog13.interp())
print(r2prog14.interp())

########### R2 Type Testing ##############
print("\nR2 Type Testing \n")
bad1 = RAdd(RBool(True), RNum(2))
bad2 = RSub(RBool(False), RNum(7))
bad3 = RAnd(RBool(True), RAdd(RNum(7), RNum(5)))
print(rTrue.typec())
print(rFalse.typec())
print(r2prog1.typec())
print(r2prog2.typec())
print(r2prog3.typec())
print(r2prog4.typec())
print(r2prog5.typec())
print(r2prog6.typec())
print(r2prog7.typec())
print(r2prog8.typec())
print(r2prog9.typec())
print(r2prog10.typec())
print(r2prog11.typec())
print(r2prog12.typec())
print(r2prog13.typec())
print(r2prog14.typec())
print(bad1.typec())
print(bad2.typec())
print(bad3.typec())

######## Random R2 Testing ########
print("\nR2 Random Testing \n")
for i in range(800):
    for n in range(0, 4):
        ranTest = optimizer(randomR2(n))
        print(ranTest.pp())
        orgAns = ranTest.interp()
        print(orgAns)
        ranTest = optimizer(ranTest)
        print(ranTest)
        print(ranTest.pp())
        print(ranTest.interp())
        s.test(isinstance(ranTest.interp(), int)
               or isinstance(ranTest.interp(), bool), (orgAns == ranTest.interp()))

######## Optimizer R2 Testing ########
optEx1 = optimizer(RNot(RNot(RBool(True))))
print(optEx1.pp() +"-->"+ str(optEx1.interp()))
optEx1 = optimizer(RIf(RIf(RBool(True), RBool(False), RBool(True)), RBool(False), RBool(True)))
print(optEx1.pp() +"-->"+ str(optEx1.interp()))
optEx1 = optimizer(RIf(RNot(RBool(True)), RBool(False), RBool(True)))
print(optEx1.pp() +"-->"+ str(optEx1.interp()))
optEx1 = optimizer(RIf(RNot(RBool(True)), RBool(True), RBool(False)))
print(optEx1.pp() +"-->"+ str(optEx1.interp()))
optEx1 = optimizer(RCmp("==", RNum(4), RNum(4)))
print(optEx1.pp() +"-->"+ str(optEx1.interp()))
optEx1 = optimizer(RCmp("<", RNum(3), RAdd(RNum(1), RNum(3))))
print(optEx1.pp() +"-->"+ str(optEx1.interp()))
optEx1 = optimizer(RIf(RCmp("==", RNum(1), RNum(2)), RBool(True), RBool(True)))
print(optEx1.pp() +"-->"+ str(optEx1.interp()))

######## Combined Testing ########
#print("\nCombined Tests\n")

# s.testAll(letTest1)
# s.testAll(letTest2)
# s.testAll(letTest3)
# s.testAll(letTest4)
# s.testAll(letTest5)
# s.testAll(letTest6)
# s.testAll(letTest7)
# s.testAll(letTest8)
# s.testAll(letTest9)
# s.testAll(letTest10)
# s.testAll(Econprog1R)
# s.testAll(Econprog2R)
# s.testAll(Econprog3R)
# s.testAll(Econprog4R)
# s.testAll(Econprog5R)
# s.testAll(Econprog6R)
# s.testAll(Rcoprog1)
# s.testAll(Rcoprog2)
# s.testAll(Rcoprog3)
# s.testAll(Rcoprog4)
# s.testAll(Rcoprog5)
# s.testAll(Rcoprog6)
# s.testAll(Uprog1)
# s.testAll(Uprog2)
# s.testAll(Uprog3)
# s.testAll(Uprog4)
# s.testAll(Uprog5)
# s.testAll(Uprog6)
# s.testAll(RAdd(RNum(22), RAdd(RNum(23), RRead())))
# s.testAll(RAdd(RNegate(RNum(22)), RNum(23)))
# s.testAll(RAdd(RNum(22), RNum(23)))
# s.testAll(RNegate(RNegate(RNum(975))))
# s.testAll(RNegate(RAdd(RNum(10), RAdd(RRead(), RNum(12)))))
# s.testAll(RNegate(RNegate(RNegate(RNegate(RNegate(RNegate(RRead())))))))
# s.testAll(RNegate(RNegate(RNegate(RNegate(RNegate(RRead()))))))
# s.testAll(RAdd(RNum(22), RAdd(RNum(23), RNum(20))))
# s.testAll(RNegate(RLet(RVar("V0"), RNegate(RLet(RVar("V0"), RNum(2), RVar(
#     "V0"))), RAdd(RAdd(RNum(2), RRead()), RAdd(RNum(4), RVar("V0"))))))


# for i in range(1):
#     s.testAll(randomR1(8))
# for i in range(1):
#     s.testAll(randomR1(7))
# for i in range(1):
#     s.testAll(randomR1(6))
# for i in range(1):
#     s.testAll(randomR1(5))
# for i in range(1):
#     s.testAll(randomR1(4))
# for i in range(1000):
#     s.testAll(randomR1(3))
# for i in range(1000):
#     s.testAll(randomR1(2))
# for i in range(1000):
#     s.testAll(randomR1(1))
# for i in range(1000):
#     s.testAll(randomR1(0))


s.endSuite()
