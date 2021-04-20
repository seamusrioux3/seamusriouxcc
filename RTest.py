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

    def testAll(self, p):
        actual = 0
        po = optimizer(p)
        pu = uniquify(po)
        palloc = exposeAllocation(pu)
        prco = RCO(palloc)
        pecon = econ(prco)
        uncov = uncoverLocal(pecon)

        if (p.interp() == pecon.interp()):
            actual = pecon.interp()
        else:
            print("original: " + p.tp())
            print("original ans: " + str(p.interp()))
            print("optimized: " + po.pp())
            print("optimized ans: " + str(po.interp()))
            print("uniquify: " + pu.pp())
            print("uniquify ans: " + str(pu.interp()))
            print("expose allocation: " + palloc.tp())
            print("expose allocation ans: " + str(palloc.interp()))
            print("rco: " + prco.tp())
            print("rco ans: " + str(prco.interp()))
            print("econ: " + pecon.pp())
            print("econ ans: " + str(prco.interp()))
            actual = not p.interp()

        self.test(actual, p.interp())

    def bigTest(self, n):
        for i in range(1000):
            self.testAll(randomR2(1))
            self.testAll(randomR2(2))
            self.testAll(randomR2(3))
            self.testAll(randomR2(4))


s = Test()
# Variable and Let testing
#print("\nR1 Tests")
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
#print("\n Uniquify Tests\n")
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
#print("\nRCO Tests\n")
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

# print(rTrue.pp())
# print(rFalse.pp())
# print(r2prog1.pp())
# print(r2prog2.pp())
# print(r2prog3.pp())
# print(r2prog4.pp())
# print(r2prog5.pp())
# print(r2prog6.pp())
# print(r2prog7.pp())
# print(r2prog8.pp())
# print(r2prog9.pp())
# print(r2prog10.pp())
# print(r2prog11.pp())
# print(r2prog12.pp())
# print(r2prog13.pp())
# print(r2prog14.pp())

########### R2 Type Testing ##############
#print("\nR2 Type Testing \n")
bad1 = RAdd(RBool(True), RNum(2))
bad2 = RSub(RBool(False), RNum(7))
bad3 = RAnd(RBool(True), RAdd(RNum(7), RNum(5)))
# print(rTrue.typec())
# print(rFalse.typec())
# print(r2prog1.typec())
# print(r2prog2.typec())
# print(r2prog3.typec())
# print(r2prog4.typec())
# print(r2prog5.typec())
# print(r2prog6.typec())
# print(r2prog7.typec())
# print(r2prog8.typec())
# print(r2prog9.typec())
# print(r2prog10.typec())
# print(r2prog11.typec())
# print(r2prog12.typec())
# print(r2prog13.typec())
# print(r2prog14.typec())
# print(bad1.typec())
# print(bad2.typec())
# print(bad3.typec())

######## Optimizer R2 Testing ########
# optEx1 = optimizer(RNot(RNot(RBool(True))))
# print(optEx1.pp() + "-->" + str(optEx1.interp()))
# optEx1 = optimizer(
#     RIf(RIf(RBool(True), RBool(False), RBool(True)), RBool(False), RBool(True)))
# print(optEx1.pp() + "-->" + str(optEx1.interp()))
# optEx1 = optimizer(RIf(RNot(RBool(True)), RBool(False), RBool(True)))
# print(optEx1.pp() + "-->" + str(optEx1.interp()))
# optEx1 = optimizer(RIf(RNot(RBool(True)), RBool(True), RBool(False)))
# print(optEx1.pp() + "-->" + str(optEx1.interp()))
# optEx1 = optimizer(RCmp("==", RNum(4), RNum(4)))
# print(optEx1.pp() + "-->" + str(optEx1.interp()))
# optEx1 = optimizer(RCmp("<", RNum(3), RAdd(RNum(1), RNum(3))))
# print(optEx1.pp() + "-->" + str(optEx1.interp()))
# optEx1 = optimizer(RIf(RCmp("==", RNum(1), RNum(2)), RBool(True), RBool(True)))
# print(optEx1.pp() + "-->" + str(optEx1.interp()))

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

######## R3 Testing #######

######## Tests With Vectors #######
# print("Vector Testing")
vec1 = RLet(RVar("x"), RNum(17), RLet(RVar("v1"), RVector([RVar("x"), RNum(1), RBool(True)]), RAdd(RVectorRef(RVar("v1"), RNum(0)), RVectorRef(RVar("v1"), RNum(1)))))
# print(vec1.pp())
# print(vec1.interp())
vec2 = RLet(RVar("x"), RNum(2), RLet(RVar("v1"), RVector([RVar("x"), RNum(1), RBool(True)]), RLet(RVar("y"), RVectorRef(RVar("v1"), RNum(1)), RAdd(RVar('y'), RNum(2)))))
# print(vec2.pp())
# print(vec2.interp())
vec3 = RLet(RVar("x"), RNum(4), RLet(RVar("v1"), RVector([RVar("x"), RNum(1), RBool(True)]), RLet(RVar("_"), RVectorSet(RVar("v1"), RNum(2), RNum(2)), RAdd(RVar("x"), RVectorRef(RVar("v1"), RNum(2))))))
# print(vec3.pp())
# print(vec3.interp())
vec4 = RLet(RVar("x"), RNum(4), RLet(RVar("v1"), RVector([RVar("x"), RNum(1), RBool(True)]), RLet(RVar("_"), RVectorSet(RVar("v1"), RNum(2), RNum(2)), RAdd(RVectorRef(RVar("v1"), RNum(1)), RVectorRef(RVar("v1"), RNum(2))))))
# print(vec4.pp())
# print(vec4.interp())
vec5 = RLet(RVar("v1"), RVector([RNum(2), RNum(2)]), RAdd(RVectorRef(RVar("v1"), RNum(0)), RVectorRef(RVar("v1"), RNum(1))))
# print(vec5.pp())
# print(vec5.interp())
vec6 = RLet(RVar("v1"), RVector([RBool(True), RNum(2), RNum(3)]), RCmp("==", RVectorRef(RVar("v1"), RNum(0)), RCmp(">", RVectorRef(RVar("v1"), RNum(1)), RVectorRef(RVar("v1"), RNum(2)))))
# print(vec6.pp())
# print(vec6.interp())

######## Tests With Typing Vectors #######
#print("\nVector Type Testing")
vec0 = RVector([RNum(1), RNum(2), RBool(True), RBool(False)])
vec7 = RLet(RVar("v1"), RVector([RBool(True), RNum(2), RNum(3)]), RAdd(RVectorRef(RVar("v1"), RNum(0)), RCmp(">", RVectorRef(RVar("v1"), RNum(1)), RVectorRef(RVar("v1"), RNum(2)))))
vec8 = RVector([RNum(1), RNum(2), RNum(3)])
vec9 = RVector([RBool(False), RBool(False), RBool(True)])
vec9 = RVector([RBool(False), RNum(3), RBool(True)])
# print(vec0.pp())
# print(vec0.typec())
# print(vec1.pp())
# print(vec1.typec())
# print(vec2.pp())
# print(vec2.typec())
# print(vec3.pp())
# print(vec3.typec())
# print(vec4.pp())
# print(vec4.typec())
# print(vec5.pp())
# print(vec5.typec())
# print(vec6.pp())
# print(vec6.typec())
# print(vec7.pp())
# print(vec7.typec())
# print(vec8.typec())
# print(vec9.typec())

######## Random Tests With Vectors #######
# print(testvec0.pp())
# print(testvec0.interp())
# for i in range(3000):
#     vec0 = randomR2(0)
#     vec1 = randomR2(1)
#     vec2 = randomR2(2)
#     print(vec0.tp())
#     print(vec0.interp(REnv()))
#     print(vec1.tp())
#     print(vec1.interp(REnv()))
#     print(vec2.tp())
#     print(vec2.interp(REnv()))


######## Big Mem Testing #######
res = bigMem(128, 1024)
# print(res.pp())
# print(res.interp())

######## Optimizer Testing #######
optvec1 = RLet(RVar("x"), RAdd(RNum(1), RNum(2)), RVectorRef(RVector([RNum(3), RNum(4)]), RNum(0)))
#print("original ans: ",optvec1.pp())
optvec1 = optimizer(optvec1)
#print("optimized ans: ", optvec1.pp())

optvec1 = RLet(RVar("x"), RAdd(RNum(7), RNum(2)), RVectorRef(RVector([RVar("x"), RNum(4)]), RNum(0)))
#print("original ans: ",optvec1.pp())
optvec1 = optimizer(optvec1)
#print("optimized ans: ", optvec1.pp())

optvec1 = RLet(RVar("x"), RNegate(RNum(7)), RVectorRef(RVector([RVar("x"), RNum(4)]), RNum(0)))
#print("original ans: ",optvec1.pp())
optvec1 = optimizer(optvec1)
#print("optimized ans: ", optvec1.pp())

optvec1 = RLet(RVar("x"), RNegate(RNum(7)), RVectorRef(RVector([RVar("x"), RNum(4)]), RRead()))
#print("original ans: ",optvec1.pp())
optvec1 = optimizer(optvec1)
#print("optimized ans: ", optvec1.pp())

optvec1 = RLet(RVar("x"), RNegate(RNum(7)), RVectorSet(RVector([RNum(3), RNum(4)]), RNum(0), RAdd(RNum(1), RNum(1))))
#print("original ans: ",optvec1.pp())
optvec1 = optimizer(optvec1)
#print("optimized ans: ", optvec1.pp())

optvec1 = RLet(RVar("x"), RVector([RNegate(RNegate(RNum(7))), RAdd(RNum(1), RNum(3))]), RVectorRef(RVar("x"), RNum(0)))
#print("original ans: ",optvec1.pp())
optvec1 = optimizer(optvec1)
#print("optimized ans: ", optvec1.pp())

######## Uniquify Testing #######
print("\nUniquify  Testing")
uni1 = RLet(RVar("VE0"), RVector([RNum(3), RBool(True)]), RLet(RVar("_"), RVectorSet( RVar("VE0"), RNum(1), RBool(False)), RCmp(">=", RRead(), RNum(13))))
print(uni1.interp())
uni1 = uniquify(optimizer(uni1))
print(uni1.pp())
print(uni1.interp())

print()
uni1 = RLet(RVar("VE0"), RVector([RNum(2), RBool(True)]), RIf(RCmp("<", RRead(), RRead()), RVectorRef(RVar("VE0"), RNum(1)), RBool(False)))
print(uni1.tp())
print(uni1.interp())
uni1 = uniquify(optimizer(uni1))
print(uni1.pp())
print(uni1.interp())

print()
uni1 = RIf(RCmp("==", RNegate(RNum(2)), RLet(RVar("V0"), RNum(10), RNum(3))), RIf(RCmp("<", RRead(), RNum(3)), RBool(True), RBool(True)), RLet(RVar("VE0"), RVector([RNum(11), RBool(False)]), RVectorRef(RVar("VE0"), RNum(1))))
print(uni1.tp())
print(uni1.interp())
uni1 = uniquify(optimizer(uni1))
print(uni1.pp())
print(uni1.interp())

print()
uni1 = RIf(RCmp("<=", RLet(RVar("V0"), RNum(13), RVar("V0")), RLet(RVar("V0"), RNum(8), RVar("V0"))), RAdd( RVar("V0"), RRead()), RNegate(RRead()))
print(uni1.tp())
print(uni1.interp())
uni1 = uniquify(optimizer(uni1))
print(uni1.pp())
print(uni1.interp())

uni1 = RIf(RCmp("<", RLet(RVar("V0"), RRead(), RVar("V0")), RLet(RVar("V0"), RRead(), RNum(13))), RIf(RCmp("<", RVar("V0"), RNum(2)), RRead(), RNum(15)), RAdd( RRead(), RNum(1)))
print(uni1.tp())
print(uni1.interp())
uni1 = uniquify(optimizer(uni1))
print(uni1.pp())
print(uni1.interp())

#### Expose Alloc Testing #####
print()
print("\nExpose Alloc Testing\n")
expall1 = RVector([RRead(), RNum(2)])
print(expall1.pp())
expall1 = exposeAllocation(expall1)
print(expall1.pp())
print(expall1.interp())
print(str(freeptr))

print()
expall1 = RVector([RRead(), RNum(2), RVector([RRead(), RNum(3)])])
print(expall1.pp())
expall1 = exposeAllocation(expall1)
print(expall1.pp())
print(expall1.interp())
print(str(freeptr))

print()
expall1 = RLet(RVar("v"), RVector([RRead(), RNum(2)]), RVectorRef(RVar("v"), RNum(0)))
print(expall1.pp())
expall1 = exposeAllocation(expall1)
print()
print(expall1.pp())
print(expall1.interp())
print(str(freeptr))

expall1 = RLet(RVar("v"), RVector([RRead(), RNum(2)]), RVectorRef(RVar("v"), RNum(0)))
print(expall1.pp())
expall1 = exposeAllocation(expall1)
print()
print(expall1.pp())
print(expall1.interp())
print(str(freeptr))

expall1 = RLet(RVar("v"), RVector([RRead(), RNum(2), RVector([RRead(), RNum(2)])]), RLet(RVar("var0"), RVectorRef(RVar("v"), RNum(0)), RLet(RVar("var1"), RVectorRef(RVar("alloc0"), RNum(0)), RAdd(RVar("var0"), RVar("var1")))))
print(expall1.pp())
expall1 = exposeAllocation(expall1)
print()
print(expall1.pp())
print(expall1.interp())

#### Expose Alloc Testing #####
print("\nRCO R3 Testing\n")

print()
rcor3prog1 =RLet(RVar("v"), RVector([RRead(), RNum(2)]), RVectorRef(RVar("v"), RNum(0)))
print(rcor3prog1.pp())
print(rcor3prog1.interp())
print()
rcor3prog1 =exposeAllocation(rcor3prog1)
print(rcor3prog1.pp())
print(rcor3prog1.interp())
rcor3prog1 =RCO(rcor3prog1)
print(rcor3prog1.pp())
print(rcor3prog1.interp())

# print()
# rcor3prog1 =RLet(RVar("v"), RVector([RRead(), RNum(2), RVector([RNum(4), RNum(2)])]), RLet(RVar("var0"), RVectorRef(RVar("v"), RNum(0)), RLet(RVar("var1"), RVectorRef(RVar("alloc0"), RNum(0)), RAdd(RVar("var0"), RVar("var1")))))
# print(rcor3prog1.pp())
# print()
# rcor3prog1 =RCO(exposeAllocation(rcor3prog1))
# print(rcor3prog1.pp())
# print(rcor3prog1.interp())

# print()
# rcor3prog1 =RLet(RVar("V0"), RLet(RVar("VE0"), RVector([RNum(4), RBool(True)]), RNum(0)), RAdd( RNum(72), RVectorRef(RVar("VE0"), RNum(0))))
# print(rcor3prog1.pp())
# print()
# rcor3prog1 =RCO(exposeAllocation(rcor3prog1))
# print(rcor3prog1.pp())
# print(rcor3prog1.interp())


######### C2 Testing #############
c2prog1 = CProgram([], {
    CLabel("main"):CBlock([], [
        CIf(CCmp("<", CAdd(CNum(freeptr), CNum(36)), CNum(fromend)),CLabel("uLabel"), CLabel("cLabel")),
        CSet(CVar("v"), CAllocate(CNum(36), "NUM")),
        CVectorSet(CVar("v"), CNum(0), CNum(2)),
        CVectorSet(CVar("v"), CNum(1), CNum(3)),
        CSet(CVar("r1"), CVectorRef(CVar("v"), CNum(0))),
        CSet(CVar("r2"), CVectorRef(CVar("v"), CNum(1))),
        CSet(CVar("r3"), CAdd(CVar("r1"), CVar("r2"))),
        CRet(CVar("r3"))
    ]),
    CLabel("uLabel"):CBlock([], [CSet(CVar("v"),CUnit()), CRet(CVar("v"))]),
    CLabel("cLabel"):CBlock([],[CSet(CVar("v"),CCollect(36)), CRet(CVar("v"))])
})

c2prog2 = CProgram([], {
    CLabel("main"):CBlock([], [
        CIf(CCmp("<", CAdd(CNum(freeptr), CNum(36)), CNum(fromend)),CLabel("uLabel"), CLabel("cLabel")),
        CSet(CVar("v"), CAllocate(CNum(36), "BOOL")),
        CVectorSet(CVar("v"), CNum(0), CBool(False)),
        CVectorSet(CVar("v"), CNum(1), CBool(True)),
        CSet(CVar("r1"), CVectorRef(CVar("v"), CNum(0))),
        CSet(CVar("r2"), CVectorRef(CVar("v"), CNum(1))),
        CRet(CVar("r2"))
    ]),
    CLabel("uLabel"):CBlock([], [CSet(CVar("v"),CUnit()), CRet(CVar("v"))]),
    CLabel("cLabel"):CBlock([],[CSet(CVar("v"),CCollect(36)), CRet(CVar("v"))])
})

c2prog3 = CProgram([], {
    CLabel("main"): CBlock(None,
                           [
                               CIf(CCmp("<", CAdd(CNum(freeptr), CNum(36)), CNum(fromend)),CLabel("uLabel"), CLabel("cLabel")),
                               CSet(CVar("v"), CAllocate(CNum(5), "NUM")),
                               CSet(CVar("x"), CNum(0)),
                               CGoto(CLabel("loop"))
                           ]),
    CLabel("loop"): CBlock(None,
                           [
                               CIf(CCmp("<", CVar("x"), CNum(4)), CLabel("inc"), CLabel("finish"))   
                           ]),
    CLabel("inc"): CBlock(None,
                          [
                              CVectorSet(CVar("v"), CVar("x"),  CNum(1)),
                              CSet(CVar("x"), CAdd(CVar("x"), CNum(1))),
                              CGoto(CLabel("loop"))
                          ]),
    CLabel("finish"): CBlock(None,
                             [
                                 CSet(CVar("r1"), CVectorRef(CVar("v"), CNum(4))),
                                 CRet(CVar("r1"))
                             ]),
    CLabel("uLabel"):CBlock([], [CSet(CVar("v"),CUnit()), CRet(CVar("v"))]),
    CLabel("cLabel"):CBlock([],[CSet(CVar("v"),CCollect(CNum(36))), CRet(CVar("v"))])
})

# print(c2prog1.interp())
# print(c2prog2.interp())
# print(c2prog3.interp())
######## Combined Testing  ########
print("\nCombined Tests\n")
s.bigTest(5)


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
