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

        print(stdout)
        ans = stdout
        if(stdout == b'true'):
            ans = 1
        elif(stdout == b'false'):
            ans = 0
        return int(ans)

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
        print(po.typec())
        t = po.typec()
        pu = uniquify(po)
        pr = RCO(pu)
        pe = econ(pr)
        xz = select(pe)
        aloc = allocate_registers(xz, t)
        # print(po.pp())
        print(aloc.emit())

        #
        #print(aloc.emit())
        machine = self.testX0OnHardware(aloc)
        # print("Machine Level Ans:", machine)
        #print("original: " + p.pp())
       # print("original ans: " + str(p.interp()))
        # print("optimized: " + po.pp())
        # print("optimized ans: " + str(po.interp()))
        # print("uniquify: " + pu.pp())
        # print("uniquify ans: " + str(pu.interp()))
        # print("rco: " + pr.pp())
        # print("rco ans: " + str(pr.interp()))
        #print("econ: " + pe.pp())
        # print("econ ans: " + str(pe.interp()))

        
        
        #print(aloc.emit())
        
        # ptch = patch(aloc)
        # real = self.testX0OnHardware(ptch)

        if (self.checkAll(p, [po, pu, pr, pe, xz, aloc], machine)):
            actual = po.interp()
        else:
            # print("original: " + p.pp())
            # print("original ans: " + str(p.interp()))
            # print("optimized: " + po.pp())
            # print("optimized ans: " + str(po.interp()))
            # print("uniquify: " + pu.pp())
            # print("uniquify ans: " + str(pu.interp()))
            # print("rco: " + pr.pp())
            # print("rco ans: " + str(pr.interp()))
            # print("econ: " + pe.pp())
            # print("econ ans: " + str(pe.interp()))
            # print("select ans: " + str(xz.interp()))
            actual = not p.interp()
            # exit(1)

        self.test(actual, p.interp())

    def bigTest(self, n):
        for i in range(100):
            self.testAll(randomR2(1))
            self.testAll(randomR2(2))
            #self.testAll(randomR2(3))


def getToX1(p):
    po = optimizer(p)
    pu = uniquify(po)
    pr = RCO(pu)
    pe = econ(pr)
    local = uncoverLocal(pe)
    xz = select(local)
    return xz


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

######## Optimizer R2 Testing ########
optEx1 = optimizer(RNot(RNot(RBool(True))))
print(optEx1.pp() + "-->" + str(optEx1.interp()))
optEx1 = optimizer(
    RIf(RIf(RBool(True), RBool(False), RBool(True)), RBool(False), RBool(True)))
print(optEx1.pp() + "-->" + str(optEx1.interp()))
optEx1 = optimizer(RIf(RNot(RBool(True)), RBool(False), RBool(True)))
print(optEx1.pp() + "-->" + str(optEx1.interp()))
optEx1 = optimizer(RIf(RNot(RBool(True)), RBool(True), RBool(False)))
print(optEx1.pp() + "-->" + str(optEx1.interp()))
optEx1 = optimizer(RCmp("==", RNum(4), RNum(4)))
print(optEx1.pp() + "-->" + str(optEx1.interp()))
optEx1 = optimizer(RCmp("<", RNum(3), RAdd(RNum(1), RNum(3))))
print(optEx1.pp() + "-->" + str(optEx1.interp()))
optEx1 = optimizer(RIf(RCmp("==", RNum(1), RNum(2)), RBool(True), RBool(True)))
print(optEx1.pp() + "-->" + str(optEx1.interp()))

########  C1 Testing  ########
cprog1 = CProgram([], {CLabel("main"): CBlock(None, [
    CSet(CVar("x"), CNum(1)),
    CSet(CVar("y"), CBool(False)),
    CSet(CVar("z"), CNot(CVar("y"))),
    CRet(CVar("z"))
])})

cprog2 = CProgram([], {
    CLabel("main"): CBlock(None,
                           [
                               CSet(CVar("x"), CNum(1)),
                               CSet(CVar("y"), CNum(2)),
                               CIf(CCmp(">=", CVar("x"), CVar("y")),
                                   CLabel("xLabel"), CLabel("yLabel")),
                           ]),
    CLabel("xLabel"): CBlock(None,
                             [
                                 CRet(CVar("x"))
                             ]),
    CLabel("yLabel"): CBlock(None,
                             [
                                 CRet(CVar("y"))
                             ])
})

cprog3 = CProgram([], {
    CLabel("main"): CBlock(None,
                           [
                               CSet(CVar("x"), CNum(1)),
                               CSet(CVar("y"), CNum(2)),
                               CIf(CCmp(">=", CVar("x"), CVar("y")),
                                   CLabel("xLabel"), CLabel("yLabel")),
                           ]),
    CLabel("xLabel"): CBlock(None,
                             [
                                 CSet(CVar("rb"), CCmp(
                                     "==", CVar("x"), CVar("y"))),
                                 CRet(CVar("rb"))
                             ]),
    CLabel("yLabel"): CBlock(None,
                             [
                                 CRet(CVar("y"))
                             ])
})

cprog4 = CProgram([], {
    CLabel("main"): CBlock(None,
                           [
                               CSet(CVar("x"), CNum(1)),
                               CSet(CVar("y"), CNum(2)),
                               #CIf(CGreaterThanEqual(CVar("x"), CVar("y")), CLabel("xLabel"), CLabel("yLabel")),
                           ]),
    CLabel("xLabel"): CBlock(None,
                             [
                                 #CSet(CVar("rb"), CEquals(CVar("x"), CVar("y"))),
                                 CRet(CVar("rb"))
                             ]),
    CLabel("yLabel"): CBlock(None,
                             [
                                 #CSet(CVar("rb"), CEquals(CVar("x"), CVar("y"))),
                                 CSet(CVar("rb"), CNot(CVar("rb"))),
                                 CRet(CVar("rb"))
                             ])
})

cprog5 = CProgram([], {CLabel("main"): CBlock(None, [
    CSet(CVar("x"), CNum(1)),
    CSet(CVar("y"), CNum(2)),
    #CSet(CVar("z"), CLessThan(CVar("x"), CVar("y"))),
    CRet(CVar("z"))
])})

cprog6 = CProgram([], {CLabel("main"): CBlock(None, [
    CSet(CVar("x"), CNum(1)),
    CSet(CVar("y"), CNum(2)),
    #CSet(CVar("z"), CGreaterThanEqual(CVar("x"), CVar("y"))),
    CRet(CVar("z"))
])})


cprog7 = CProgram([], {
    CLabel("main"): CBlock(None,
                           [
                               CSet(CVar("x"), CNum(1)),
                               CGoto(CLabel("loop"))
                           ]),
    CLabel("loop"): CBlock(None,
                           [
                               #CIf(CLessThan(CVar("x"), CNum(5)), CLabel("inc"), CLabel("finish"))
                           ]),
    CLabel("inc"): CBlock(None,
                          [
                              CSet(CVar("x"), CAdd(CVar("x"), CNum(1))),
                              CGoto(CLabel("loop"))
                          ]),
    CLabel("finish"): CBlock(None,
                             [
                                 CRet(CVar("x"))
                             ])
})

# print(cprog1.pp())
# print("Ans: " + str(cprog1.interp()))
# print(cprog2.pp())
# print("Ans: " + str(cprog2.interp()))
# print(cprog3.pp())
# print("Ans: " + str(cprog3.interp()))
# print(cprog4.pp())
# print("Ans: " + str(cprog4.interp()))
# print(cprog5.pp())
# print("Ans: " + str(cprog5.interp()))
# print(cprog6.pp())
# print("Ans: " + str(cprog6.interp()))
# print(cprog7.pp())
# print("Ans: " + str(cprog7.interp()))

########  X1 Testing  ########
print("\nX1  Testing")


xprog1 = XProgram([], {XLabel("main"):
                       XBlock(None, [
                           XIMov(XCon(1), XRegister("rax")),
                           XIXor(XCon(1), XRegister("rax")),
                           XIRet()
                       ])
                       })

xprog2 = XProgram([], {XLabel("main"):
                       XBlock(None, [
                           XIMov(XCon(0), XRegister("rax")),
                           XIMov(XCon(0), XRegister("rbx")),
                           XIXor(XRegister("rbx"), XRegister("rax")),
                           XIRet()
                       ])
                       })

xprog3 = XProgram([], {XLabel("main"):
                       XBlock(None, [
                           XIMov(XCon(1), XRegister("rax")),
                           XIMov(XCon(0), XRegister("rbx")),
                           XIXor(XRegister("rbx"), XRegister("rax")),
                           XIMov(XCon(1), XRegister("rbx")),
                           XIXor(XRegister("rbx"), XRegister("rax")),
                           XIRet()
                       ])
                       })

xprog4 = XProgram([], {
    XLabel("main"):
    XBlock(None, [
        XIMov(XCon(3), XRegister("rcx")),
        XIMov(XCon(2), XRegister("rbx")),
        XICmp(XRegister("rcx"), XRegister("rbx")),
        XIJmpIf(XGEq(), XLabel("ltrue")),
        XIRet()
    ]),
    XLabel("ltrue"):
    XBlock(None, [
        XIMov(XCon(3), XRegister("rax")),
        XIRet()
    ])
})

xprog5 = XProgram([], {
    XLabel("main"):
    XBlock(None, [
        XIMov(XCon(3), XRegister("rcx")),
        XIMov(XCon(2), XRegister("rbx")),
        XICmp(XRegister("rcx"), XRegister("rbx")),
        XIJmpIf(XL(), XLabel("ltrue")),
        XICmp(XRegister("rcx"), XRegister("rbx")),
        XIJmpIf(XG(), XLabel("lfalse")),
        XIRet()
    ]),
    XLabel("ltrue"):
    XBlock(None, [
        XIMov(XCon(3), XRegister("rax")),
        XIRet()
    ]),
    XLabel("lfalse"):
    XBlock(None, [
        XIMov(XCon(0), XRegister("rax")),
        XIRet()
    ])
})

xprog6 = XProgram([], {
    XLabel("main"):
    XBlock(None, [
        XIMov(XCon(3), XRegister("rcx")),
        XIMov(XCon(2), XRegister("rbx")),
        XICmp(XRegister("rcx"), XRegister("rbx")),
        XIJmpIf(XG(), XLabel("ltrue")),
        XICmp(XRegister("rcx"), XRegister("rbx")),
        XIJmpIf(XL(), XLabel("lfalse")),
        XIRet()
    ]),
    XLabel("ltrue"):
    XBlock(None, [
        XIMov(XCon(3), XRegister("rax")),
        XIRet()
    ]),
    XLabel("lfalse"):
    XBlock(None, [
        XIMov(XCon(0), XRegister("rax")),
        XIRet()
    ])
})

xprog7 = XProgram([], {
    XLabel("main"): XBlock(None,
                           [
                               XIMov(XCon(1), XRegister("rbx")),
                               XIJmp(XLabel("loop"))
                           ]),
    XLabel("loop"): XBlock(None,
                           [
                               XIMov(XCon(5), XRegister("rcx")),
                               XICmp(XRegister("rbx"), XRegister("rcx")),
                               XIJmpIf(XL(), XLabel("inc")),
                               XIJmp(XLabel("finish"))
                           ]),
    XLabel("inc"): XBlock(None,
                          [
                              XIAdd(XCon(1), XRegister("rbx")),
                              XIJmp(XLabel("loop"))
                          ]),
    XLabel("finish"): XBlock(None,
                             [
                                 XIMov(XRegister("rbx"), XRegister("rax")),
                                 XIRet()
                             ])
})

xprog8 = XProgram([], {XLabel("main"):
                       XBlock(None, [
                           XIMovzb(XCon(20), XByteRegister("al")),
                           XIMovzb(XByteRegister("al"), XRegister("rax")),
                           XIRet()
                       ])
                       })

xprog9 = XProgram([], {XLabel("main"):
                       XBlock(None, [
                           XIMov(XCon(1), XVar("x")),
                           XIMov(XCon(2), XVar("y")),
                           XICmp(XVar("x"), XVar("y")),
                           XISet(XG(), XByteRegister("al")),
                           XIMov(XByteRegister("al"), XRegister("rax")),
                           XIMov(XCon(3), XVar("x")),
                           XIMov(XCon(2), XVar("y")),
                           XICmp(XVar("x"), XVar("y")),
                           XISet(XG(), XByteRegister("al")),
                           XIMov(XByteRegister("al"), XRegister("rax")),
                           XIRet()
                       ])
                       })



######## Tests With Alloc #######
alc0 = RNegate(RIf(RCmp(">=", RNum(11), RNum(0)), RNum(14), RNum(2)))

######## Tests With Conditional Moves #######
def getToEcon(x):
    return  RCO(uniquify(optimizer(x)))
condMov1 = RLet(RVar("x"), RIf(RCmp("<", RNum(12), RNum(13)), RNum(5), RNum(6)), RVar("x"))
condMov1 = getToEcon(condMov1)
# print(condMov1.pp())
# print(condMov1.interp())
condMov1 = econ(condMov1)
# print(condMov1.pp())
# print(condMov1.interp())
condMov1 = select(condMov1)
# print(condMov1.emit())
# print(condMov1.interp())

######## Tests With Vectors #######
print("Vector Testing")
vec1 = RLet(RVar("x"), RNum(17), RLet(RVar("v1"), RVector(RVar("x"), RNum(1), RBool(True)), RAdd(RVectorRef(RVar("v1"), RNum(0)), RVectorRef(RVar("v1"), RNum(1)))))
print(vec1.pp())
print(vec1.interp())
vec2 = RLet(RVar("x"), RNum(2), RLet(RVar("v1"), RVector(RVar("x"), RNum(1), RBool(True)), RLet(RVar("y"), RVectorRef(RVar("v1"), RNum(1)), RAdd(RVar('y'), RNum(2)))))
print(vec2.pp())
print(vec2.interp())
vec3 = RLet(RVar("x"), RNum(4), RLet(RVar("v1"), RVector(RVar("x"), RNum(1), RBool(True)), RLet(RVar("_"), RVectorSet(RVar("v1"), RNum(2), RNum(2)), RAdd(RVar("x"), RVectorRef(RVar("v1"), RNum(2))))))
print(vec3.pp())
print(vec3.interp())
vec4 = RLet(RVar("x"), RNum(4), RLet(RVar("v1"), RVector(RVar("x"), RNum(1), RBool(True)), RLet(RVar("_"), RVectorSet(RVar("v1"), RNum(2), RNum(2)), RAdd(RVectorRef(RVar("v1"), RNum(1)), RVectorRef(RVar("v1"), RNum(2))))))
print(vec4.pp())
print(vec4.interp())
vec5 = RLet(RVar("v1"), RVector(RNum(2), RNum(2)), RAdd(RVectorRef(RVar("v1"), RNum(0)), RVectorRef(RVar("v1"), RNum(1))))
print(vec5.pp())
print(vec5.interp())
vec6 = RLet(RVar("v1"), RVector(RBool(True), RNum(2), RNum(3)), RCmp("==", RVectorRef(RVar("v1"), RNum(0)), RCmp(">", RVectorRef(RVar("v1"), RNum(1)), RVectorRef(RVar("v1"), RNum(2)))))
print(vec6.pp())
print(vec6.interp())

######## Tests With Typing Vectors #######
print("\nVector Type Testing")
vec0 = RVector(RNum(1), RNum(2), RBool(True), RBool(False))
vec7 = RLet(RVar("v1"), RVector(RBool(True), RNum(2), RNum(3)), RAdd(RVectorRef(RVar("v1"), RNum(0)), RCmp(">", RVectorRef(RVar("v1"), RNum(1)), RVectorRef(RVar("v1"), RNum(2)))))
print(vec0.pp())
print(vec0.typec())
print(vec1.pp())
print(vec1.typec())
print(vec2.pp())
print(vec2.typec())
print(vec3.pp())
print(vec3.typec())
print(vec4.pp())
print(vec4.typec())
print(vec5.pp())
print(vec5.typec())
print(vec6.pp())
print(vec6.typec())
print(vec7.pp())
print(vec7.typec())

######## Combined Testing Updated With R2 Uniquify ########
#print("\nCombined Tests\n")
#s.bigTest(5)

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
# s.testAll(RLet(RVar("R1"), RAdd(RNum(1), RNum(1)), RLet(RVar("R2"), RAdd(RVar(
#     "R1"), RVar("R1")), RLet(RVar("R3"), RAdd(RVar("R2"), RVar("R2")), RVar("R3")))))
# s.testAll(RLet(RVar("R1"), RAdd(RNegate(RNum(2)),
#                                 RNegate(RNegate(RNum(2)))), RVar("R1")))
# s.testAll(RLet(RVar("R1"), RNum(4), RVar("R1")))
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


s.endSuite()
