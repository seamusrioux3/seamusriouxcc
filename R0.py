import random
from datetime import datetime
from graph import Vertex, Graph
# R0 Data types


class REnv:
    def __init__(self):
        self.env = {}

    def getEnv(self):
        return self.env

    def setEnv(self, left, right):
        self.env[left] = right


class RNum:
    def __init__(self, _num):
        self.num = _num

    def pp(self):
        return str(self.num)

    def interp(self, e=None):
        return self.num

    def typec(self, env=None):
        return "NUM"


class RNegate:
    def __init__(self, _num):
        self.num = _num

    def pp(self):
        return "-(" + str(self.num.pp()) + ")"

    def interp(self, e=None):
        return -1*self.num.interp(e)

    def typec(self, env=None):
        if(self.num.typec(env) == "NUM"):
            return "NUM"
        return "ERROR"


class RAdd:
    def __init__(self, _left, _right):
        self.left = _left
        self.right = _right

    def pp(self):
        return "(+ " + self.left.pp() + " " + self.right.pp() + ")"

    def interp(self, e=None):
        return self.left.interp(e) + self.right.interp(e)

    def typec(self, env=None):
        if(self.left.typec(env) == self.right.typec(env) == "NUM"):
            return self.left.typec(env)
        return "ERROR"


class RRead:
    def __init__(self):
        self.num = 0

    def pp(self):
        return "Read"

    def interp(self,  e=None):
        return 1
        inp = input("Read: ")
        if(inp == ""):
            self.num = 1
        else:
            self.num = int(inp)
        return self.num

    def typec(self, env=None):
        return "NUM"


###### R1 data types ######


class RVar:
    def __init__(self, _name):
        self.name = _name

    def pp(self):
        return str(self.name)

    def interp(self, e=None):
        if(self.name in e.getEnv()):
            return e.getEnv()[self.name]
        return "ERROR"

    def typec(self, env=None):
        if(self.name in env.getEnv()):
            return env.getEnv()[self.name]
        return "ERROR"


class RLet:
    def __init__(self, _var, _l, _r):
        self.var = _var
        self.l = _l
        self.r = _r

    def pp(self):
        return "Let " + self.var.pp() + " = " + self.l.pp() + " in " + self.r.pp()

    def interp(self, e=None):
        if(not e):
            e = REnv()
        e.setEnv(self.var.name, self.l.interp(e))
        return self.r.interp(e)

    def typec(self, env=None):
        if(not env):
            env = REnv()
        env.setEnv(self.var.name, self.l.typec(env))
        if(self.l.typec(env) == self.r.typec(env)):
            return self.l.typec(env)
        return "ERROR"


###### R2 data types ######

class RAnd:
    def __init__(self, _l, _r):
        self.l = _l
        self.r = _r

    def pp(self):
        return "(and " + self.l.pp() + " " + self.r.pp() + ")"

    def interp(self, env=None):
        return self.l.interp(env) and self.r.interp(env)

    def typec(self, env=None):
        if(self.l.typec(env) == self.r.typec(env) == "BOOL"):
            return self.l.typec(env)
        return "ERROR"


class ROr:
    def __init__(self, _l, _r):
        self.l = _l
        self.r = _r

    def pp(self):
        return "(or " + self.l.pp() + " " + self.r.pp() + ")"

    def interp(self, env=None):
        return self.l.interp(env) or self.r.interp(env)

    def typec(self, env=None):
        if(self.l.typec(env) == self.r.typec(env) == "BOOL"):
            return self.l.typec(env)
        return "ERROR"


class RNot:
    def __init__(self, _e):
        self.e = _e

    def pp(self):
        return "(not " + self.e.pp() + ")"

    def interp(self, env=None):
        return not self.e.interp(env)

    def typec(self, env=None):
        if(self.e.typec(env) == "BOOL"):
            return self.e.typec(env)
        return "ERROR"


class RCmp:
    def __init__(self, _op, _l, _r):
        self.op = _op
        self.l = _l
        self.r = _r

    def pp(self):
        return "(" + self.op + " " + self.l.pp() + " " + self.r.pp() + ")"

    def interp(self, env=None):
        if(self.op == "=="):
            return self.l.interp(env) == self.r.interp(env)
        elif(self.op == ">="):
            return self.l.interp(env) >= self.r.interp(env)
        elif(self.op == ">"):
            return self.l.interp(env) > self.r.interp(env)
        elif(self.op == "<="):
            return self.l.interp(env) <= self.r.interp(env)
        elif(self.op == "<"):
            return self.l.interp(env) < self.r.interp(env)
        return "ERROR"

    def typec(self, env=None):
        return "BOOL"


class RIf:
    def __init__(self, _var, _l, _r):
        self.var = _var
        self.l = _l
        self.r = _r

    def pp(self):
        return "(if " + self.var.pp() + " " + self.l.pp() + " " + self.r.pp() + ")"

    def interp(self, env=None):
        return self.l.interp(env) if self.var.interp(env) else self.r.interp(env)

    def typec(self, env=None):
        if(self.var.interp(env)):
            return self.l.typec(env)
        else:
            return self.r.typec(env)


class RSub:
    def __init__(self, _l, _r):
        self.l = _l
        self.r = _r

    def pp(self):
        return "(- " + self.l.pp() + " " + self.r.pp() + ")"

    def interp(self, env=None):
        return self.l.interp(env) - self.r.interp(env)

    def typec(self, env=None):
        if(self.l.typec(env) == self.r.typec(env) == "NUM"):
            return self.l.typec(env)
        return "ERROR"


class RBool:
    def __init__(self, _b):
        self.b = _b

    def pp(self):
        return str(self.b)

    def interp(self, env=None):
        return self.b

    def typec(self, env=None):
        return "BOOL"


class RS64:
    def __init__(self, _s):
        self.s = _s

    def pp(self):
        return str(self.s)

    def interp(self, env=None):
        return self.s


############ X0 Programs ############


class XEnv:
    def __init__(self):
        self.reg = {}
        self.var = {}
        self.mem = {}
        self.blk = {}
        self.cntr = 0


class XProgram:
    def __init__(self, _info, _p):
        self.p = _p
        self.info = _info

    def emit(self):
        return ".global main\n\n" + "".join(["\n"+x.emit() + ":" + "\n" + y.emit() for x, y in self.p.items()])

    def interp(self):
        env = XEnv()
        for a, b in self.p.items():
            env.blk[a.interp(env)] = b
        if("main" in env.blk):
            env.blk["main"].interp(env)
        else:
            env.blk[next(iter(env.blk))].interp(env)
        # print(env.reg)
        # print(env.var)
        # print(env.mem)
        # print(env.blk)
        # print(env.cntr)
        return env.reg["rax"]


class XBlock:
    def __init__(self, _aux, _blk):
        self.blk = _blk
        self.aux = _aux

    def emit(self):
        return "\n".join(x.emit() for x in self.blk)

    def interp(self, env):
        for a in self.blk:
            a.interp(env)
        return env


class XLabel:
    def __init__(self, _string):
        self.string = _string

    def emit(self):
        return self.string

    def interp(self, env):
        return self.string


class XVar:
    def __init__(self, _name):
        self.name = _name

    def emit(self):
        return "!" + self.name

    def interp(self, env):
        return env.var[self.name]

    def set(self, env, val):
        env.var[self.name] = val

    def getName(self):
        return self.name


class XRegister:
    def __init__(self, _register):
        ######## Register must be strictly these ########
        if(_register.lower() in ["rsp", "rbp", "rax", "rbx", "rcx", "rdx", "rsi", "rdi", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15"]):
            self.register = _register
        else:
            print(_register.lower())
            print("\nINVALID REGISTER\n")

    def emit(self):
        return "%" + self.register

    def interp(self, env):
        if(self.register in env.reg.keys()):
            return env.reg[self.register]
        else:
            env.reg[self.register] = 0
            return env.reg[self.register]

    def set(self, env, val):
        env.reg[self.register] = val

    def getName(self):
        return self.register


########### Register Value Set up ##############
allRegs = [XRegister("rsp"), XRegister("rbp"), XRegister("rax"), XRegister("rbx"), XRegister("rcx"), XRegister("rdx"), XRegister("rsi"),
           XRegister("rdi"), XRegister("r8"), XRegister("r9"), XRegister(
               "r10"), XRegister("r11"), XRegister("r12"), XRegister("r13"),
           XRegister("r14"), XRegister("r15")]
calleeSavedRegs = [XRegister("r12"), XRegister(
    "r13"), XRegister("r14"), XRegister("r15")]
callerSavedRegs = [XRegister("rax"), XRegister("rcx"), XRegister("rdx"), XRegister("rsi"), XRegister("rdi"), XRegister("r8"), XRegister("r9"),
                   XRegister("r10"), XRegister("r11")]
argumentRegs = [XRegister("rdi"), XRegister("rsi"), XRegister(
    "rdx"), XRegister("rcx"), XRegister("r8"), XRegister("r9")]
usableRegs = [XRegister("rbx"), XRegister("rcx"), XRegister("rdx"), XRegister("rsi"),
              XRegister("rdi"), XRegister("r8"), XRegister("r9"), XRegister(
                  "r10"), XRegister("r11"), XRegister("r12"), XRegister("r13"),
              XRegister("r14"), XRegister("r15")]
tempReg = XRegister("rax")


class XCon:
    def __init__(self, _value):
        self.value = _value

    def emit(self):
        return "$" + str(self.value)

    def interp(self, env):
        return self.value


class XMem:
    def __init__(self, _reg, _num):
        self.reg = _reg
        self.num = _num

    def emit(self):
        return str(self.num) + "(" + str(self.reg.emit()) + ")"

    def interp(self, env):
        if(self.reg.interp(env) + self.num in env.mem.keys()):
            return env.mem[self.reg.interp(env) + self.num]
        else:
            env.mem[self.reg.interp(env) + self.num] = 0
            return env.mem[self.reg.interp(env) + self.num]

    def set(self, env, val):
        env.mem[self.reg.interp(env) + self.num] = val
        return env

    def getName(self):
        return self.reg


############ Instructions ############
class XIAdd:
    def __init__(self, _src, _dst):
        self.src = _src
        self.dst = _dst

    def emit(self):
        return "addq" + " " + self.src.emit() + ", " + self.dst.emit()

    def interp(self, env):
        env = self.dst.set(env, self.src.interp(env) + self.dst.interp(env))
        return env


class XISub:
    def __init__(self, _src, _dst):
        self.src = _src
        self.dst = _dst

    def emit(self):
        return "subq" + " " + self.src.emit() + ", " + self.dst.emit()

    def interp(self, env):
        env = self.dst.set(env, self.dst.interp(env) - self.src.interp(env))
        return env


class XIMov:
    def __init__(self, _src, _dst):
        self.src = _src
        self.dst = _dst

    def emit(self):
        return "movq" + " " + self.src.emit() + ", " + self.dst.emit()

    def interp(self, env):
        env = self.dst.set(env, self.src.interp(env))
        return env


class XIRet:
    def __init__(self, _src=None):
        self.src = _src

    def emit(self):
        return "retq"

    def interp(self, env):
        return env


class XINeg:
    def __init__(self, _src):
        self.src = _src

    def emit(self):
        return "negq" + " " + self.src.emit()

    def interp(self, env):
        env = self.src.set(env, -1*self.src.interp(env))
        return env


class XICall:
    def __init__(self, _src):
        self.src = _src

    def emit(self):
        return "callq" + " " + self.src.emit()

    def interp(self, env):
        temp = self.src.interp(env)
        if(temp == "read_int"):
            env.cntr = 1
            XIMov(XCon(env.cntr), XRegister("rax")).interp(env)
        elif(temp == "print_int"):
            pass
            # print(env.reg["RDI"])
        else:
            env.blk[temp].interp(env)
        return env


class XIJmp:
    def __init__(self, _src):
        self.src = _src

    def emit(self):
        return "jmp" + " " + self.src.emit()

    def interp(self, env):
        env.blk[self.src.interp(env)].interp(env)
        return env


class XIPush:
    def __init__(self, _src):
        self.src = _src

    def emit(self):
        return "pushq" + " " + self.src.emit()

    def interp(self, env):
        XISub(XCon(8), XRegister("RSP")).interp(env)
        XIMov(self.src, XMem(XRegister("RSP"), 0)).interp(env)
        return


class XIPop:
    def __init__(self, _src):
        self.src = _src

    def emit(self):
        return "popq" + " " + self.src.emit()

    def interp(self, env):
        XIMov(XMem(XRegister("RSP"), 0), self.src).interp(env)
        XIAdd(XCon(8), XRegister("RSP")).interp(env)
        return

###### C0 Program Data Types ########


class CEnv:
    def __init__(self):
        self.var = {}
        self.blk = {}
        self.cntr = 0

    def setBlk(self, add):
        self.blk.update(add)

    def setVar(self, add):
        self.var.update(add)


class CProgram:
    def __init__(self, _info=None, _p=None):
        self.p = _p
        self.info = _info

    def pp(self):
        return "".join(["\n" + l.pp() + ":" + b.pp() for l, b in self.p.items()])

    def interp(self):
        tempBlks = {}
        for i, j in self.p.items():
            tempBlks.update({i.interp(): j})
        env = CEnv()
        env.setBlk(tempBlks)
        rtn = 0
        rtn = env.blk["main"].interp(env)
        return rtn


class CBlock:
    def __init__(self, _aux, _p):
        self.p = _p
        self.aux = _aux

    def pp(self):
        return "".join(["\n" + i.pp() for i in self.p])

    def interp(self, env):
        rtn = 0
        for i in self.p:
            rtn = i.interp(env)
        return rtn


class CLabel:
    def __init__(self, _label):
        self.label = _label

    def pp(self):
        return self.label

    def interp(self):
        return self.label


class CRet:
    def __init__(self, _var):
        self.var = _var

    def pp(self):
        return "return " + self.var.pp()

    def interp(self, env):
        return env.var[self.var.pp()]


class CNum:
    def __init__(self, _n):
        self.n = _n

    def pp(self):
        return str(self.n)

    def interp(self, env):
        return self.n


class CVar:
    def __init__(self, _var):
        self.var = _var

    def pp(self):
        return self.var

    def interp(self, env):
        return env.var[self.var]


class CRead:
    def __init__(self):
        self.r = 0

    def pp(self):
        return "Read"

    def interp(self, env):
        return 1
        env.cntr += 1
        return env.cntr


class CNeg:
    def __init__(self, _n):
        self.n = _n

    def pp(self):
        return "-("+self.n.pp() + ")"

    def interp(self, env):
        return -1 * self.n.interp(env)


class CAdd:
    def __init__(self, _l, _r):
        self.l = _l
        self.r = _r

    def pp(self):
        return "(+ " + self.l.pp() + " " + self.r.pp() + ")"

    def interp(self, env):
        return self.l.interp(env) + self.r.interp(env)


class CSet:
    def __init__(self, _var, _exp):
        self.var = _var
        self.exp = _exp

    def pp(self):
        return "(set! " + self.var.pp() + " " + self.exp.pp() + ")"

    def interp(self, env):
        env.setVar({self.var.pp(): self.exp.interp(env)})
        return 0


###################### Functions ######################


def randomR2(n):
    random.seed(datetime.now())
    r = random.choice([_randomR2Bool(n, []), _randomR2(n, [])])
    return r


def _randomR2(n, v):
    random.seed(datetime.now())
    ret = 0
    ranNum = RNum(random.randint(0, 16))
    def ranNeg(n): return RNegate(_randomR2(n-1, v))
    def ranAdd(n): return RAdd(_randomR2(n-1, v), _randomR2(n-1, v))
    def ranSub(n): return RSub(_randomR2(n-1, v), _randomR2(n-1, v))
    if(n == 0):
        if(v):
            chosenVar = random.choice(v)
            ret = random.choice(
                [ranNum, chosenVar, RRead()])
        else:
            ret = random.choice([ranNum, RRead()])
    else:

        ret = random.choice(
            [ranAdd(n), ranNeg(n), ranLet("NUM", n, v), ranSub(n), ranIf(n, v)])
    return ret


def _randomR2Bool(n, v):
    random.seed(datetime.now())
    ret = 0
    ranBool = RBool(random.choice([True, False]))
    def ranNot(n): return RNot(_randomR2Bool(n-1, v))
    def ranAnd(n): return RAnd(_randomR2Bool(n-1, v), _randomR2Bool(n-1, v))
    def ranOR(n): return ROr(_randomR2Bool(n-1, v), _randomR2Bool(n-1, v))
    def ranCmp(n): return RCmp(random.choice(
        ["==", ">=", ">", "<=", "<"]), _randomR2(n-1, v), _randomR2(n-1, v))
    if(n == 0):
        if(v):
            chosenVar = random.choice(v)
            ret = random.choice(
                [chosenVar, ranBool])
        else:
            ret = random.choice([ranBool])
    else:

        ret = random.choice([ranNot(n), ranAnd(n), ranOR(
            n), ranCmp(n), ranLet("BOOL", n, v), ranIf(n, v)])
    return ret


def ranLet(t, n, v):
    newVar = RVar("V" + str(len(v)))
    if(t == "BOOL"):
        return RLet(newVar,  _randomR2Bool(n-1, []),  _randomR2Bool(n-1, []))
    elif(t == "NUM"):
        return RLet(newVar,  _randomR2(n-1, []),  _randomR2(n-1, []))
    print("ERROR in RAN")
    exit(1)
    return "ERROR"


def ranIf(n, v):
    return RIf(_randomR2Bool(n-1, v), random.choice([_randomR2(n-1, v), _randomR2Bool(n-1, v)]), random.choice([_randomR2(n-1, v), _randomR2(n-1, v)]))


######## Optimizer Function ########


class OptEnv:
    def __init__(self):
        self.env = {}

    def getEnv(self):
        return self.env

    def setEnv(self, add):
        self.env.update(add)


def simple(n):
    if(isinstance(n, RNum)):
        return True
    elif(isinstance(n, RRead)):
        return False
    elif(isinstance(n, RNegate)):
        return simple(n.num)
    elif(isinstance(n, RAdd)):
        return simple(n.left) and simple(n.right)
    elif(isinstance(n, RVar)):
        return True
    elif(isinstance(n, RLet)):
        return simple(n.l) and simple(n.r)


def optimizer(n):
    env = OptEnv()
    return _optimizer(n, env)


def _optimizer(n, env):
    if isinstance(n, RNum):
        return n
    elif isinstance(n, RBool):
        return n
    elif isinstance(n, RRead):
        return n
    elif(isinstance(n,RCmp)):
        op = n.op
        l = n.l
        r = n.r
        if(isinstance(l,RNum) and isinstance(r,RNum) and op == "==" and l.interp() == r.interp()):
            return RBool(n.interp())
        elif(op == "<"):
            if(isinstance(r,RAdd) and isinstance(r.left,RNum)):
                if(r.right.interp() == l.interp() and r.left.interp() > 0):
                    return RBool(True)
        return n
    elif(isinstance(n, RNot)):
        if(isinstance(n.e, RNot)):
            return _optimizer(n.e.e, env)
        return RNot(_optimizer(n.e, env)) 
    elif isinstance(n, RNegate):
        e = n.num
        if(isinstance(e, RNum)):
            return RNum(-1 * e.num)
        elif(isinstance(e, RNegate)):
            return _optimizer(e.num, env)
        elif(isinstance(e, RAdd)):
            if(isinstance(e.left, RNum)):
                return RAdd(RNum(-1*e.left.num), RNegate(_optimizer(e.right, env)))
            else:
                return RNegate(_optimizer(e, env))
        else:
            return RNegate(_optimizer(e, env))
    elif isinstance(n, RAdd):
        l = n.left
        r = n.right
        if(isinstance(l, RNum) and isinstance(r, RNum)):
            print("Add case 1")
            return RNum(l.interp() + r.interp())

        elif(isinstance(l, RNum) and isinstance(r, RAdd) and isinstance(r.left, RNum)):
            print("Add case 2")
            return RAdd(RNum(l.interp() + r.left.interp()), _optimizer(r.right, env))

        elif(isinstance(l, RAdd) and isinstance(r, RNum) and isinstance(l.left, RNum)):
            print("Add case 3")
            return RAdd(RNum(l.left.interp() + r.interp()), _optimizer(l.right, env))

        elif(isinstance(l, RAdd) and isinstance(l.left, RNum) and isinstance(r, RAdd) and isinstance(r.left, RNum)):
            print("Add case 4")
            return RAdd(RNum(l.left.interp() + r.left.interp()), RAdd(_optimizer(l.right, env), _optimizer(r.right, env)))

        elif(not isinstance(l, RNum) and isinstance(r, RNum)):
            print("Add case 5")
            return RAdd(r, _optimizer(l, env))
        else:
            print("Add case 6")
            return RAdd(_optimizer(l, env), _optimizer(r, env))
    elif(isinstance(n, RIf)):
        var = n.var
        l = n.l
        r = n.r
        if(l.interp() == True and r.interp() == False):
            return _optimizer(var, env)
        elif(isinstance(var, RIf) and var.l.interp() == False and var.r.interp() == True):
            if(l.interp() == False and r.interp() == True):
                return _optimizer(var.var, env)
        elif(isinstance(var, RNot)):
            return RIf(var.e, r, l)
        elif(l.interp() == r.interp()):
            return RLet(RVar("_"), var, l)
        
        return RIf(_optimizer(var,env), _optimizer(l,env), _optimizer(r,env))

    elif(isinstance(n, RVar)):
        if(n.name in env.getEnv()):
            return env.getEnv()[n.name]
        else:
            return n
    elif(isinstance(n, RLet)):
        xe = _optimizer(n.l, env)
        if(simple(xe)):
            env.setEnv({n.var.name: xe})
            return _optimizer(n.r, env)
        else:
            env.setEnv({n.var.name: xe})
            be = _optimizer(n.r, env)
            return RLet(n.var, xe, be)

    return n

######## Uniquify Function ########


class UNEnv:
    def __init__(self):
        self.varCntr = 0
        self.env = {}

    def setEnv(self, add):
        self.env.update(add)

    def getEnv(self):
        return self.env


def uniquify(e):
    env = UNEnv()
    e = uni(e, env)
    return e


def uni(e, uenv):
    if(isinstance(e, RNum)):
        return e
    elif(isinstance(e, RRead)):
        return e
    elif(isinstance(e, RNegate)):
        return RNegate(uni(e.num, uenv))
    elif(isinstance(e, RAdd)):
        return RAdd(uni(e.left, uenv), uni(e.right, uenv))
    elif(isinstance(e, RVar)):
        if e.pp() in uenv.getEnv():
            return RVar(uenv.getEnv()[e.pp()])
        else:
            print("UNI VAR UNBOUND")
            return "FAILURE"
    elif(isinstance(e, RLet)):
        uenv.varCntr += 1
        x = RVar("U"+str(uenv.varCntr))
        l = uni(e.l, uenv)
        uenv.setEnv({e.var.pp(): x.pp()})
        r = uni(e.r, uenv)
        return RLet(x, l, r)

    return 0


########### Resolve Complex ###########


class RCOEnv:
    def __init__(self):
        self.varCntr = 0
        self.lifts = []
        self.env = {}

    def getEnv(self):
        return self.env

    def setEnv(self, add):
        self.env.update(add)

    def getLift(self):
        return self.lifts

    def setLift(self, add):
        self.lifts.insert(0, add)

    def incCntr(self):
        self.varCntr += 1
        return self.varCntr


def RCO(e):
    env = RCOEnv()
    rtn = _rco(env, e)
    return letStar(rtn, env)


def _rcoLift(env, e):
    indx = env.incCntr()
    nv = "R" + str(indx)
    env.setLift((RVar(nv), e))
    return RVar(nv)


def _rco(env, e):
    if(isinstance(e, RNum)):
        return _rcoLift(env, e)
    elif(isinstance(e, RRead)):
        return _rcoLift(env, e)

    elif(isinstance(e, RNegate)):
        ep = _rco(env, e.num)
        return _rcoLift(env, RNegate(ep))

    elif(isinstance(e, RAdd)):
        lp = _rco(env, e.left)
        rp = _rco(env, e.right)
        return _rcoLift(env, RAdd(lp, rp))

    elif(isinstance(e, RVar)):
        if(e.name in env.getEnv()):
            return env.getEnv()[e.name]
        else:
            print("RCO UNBOUND")
            return "FAILURE"

    elif(isinstance(e, RLet)):
        lp = _rco(env, e.l)
        env.setEnv({e.var.name: lp})
        return _rco(env, e.r)


def letStar(fa, env):
    if not env.getLift():
        return fa
    else:
        var, eq = env.getLift().pop()
        return RLet(var, eq, letStar(fa, env))


######## Explicate Control Pass ########
class EconEnv:
    def __init__(self):
        self.p = []

    def addEnv(self, a):
        self.p.append(a)

    def getEnv(self):
        return self.p


def econ(r):
    env = EconEnv()
    rtn = econHelper(r, env)
    env.addEnv(rtn)
    p = CProgram(None, {CLabel("main"): CBlock([], env.getEnv())})
    return p


def econArgs(r):
    if(isinstance(r, RNum)):
        return CNum(r.num)
    elif(isinstance(r, RVar)):
        return CVar(r.name)
    else:
        return "ERROR"


def econExp(r):
    if(isinstance(r, RRead)):
        return CRead()
    elif(isinstance(r, RNegate)):
        return CNeg(econArgs(r.num))
    elif(isinstance(r, RAdd)):
        return CAdd(econArgs(r.left), econArgs(r.right))
    else:
        return econArgs(r)


def econHelper(r, env):
    if(isinstance(r, RLet)):
        a = CSet(econArgs(r.var), econExp(r.l))
        env.addEnv(a)
        return econHelper(r.r, env)
    elif(isinstance(r, RVar)):
        return CRet(econArgs(r))
    else:
        return CRet(r)


######## Select Instr Pass ########

class SelEnv:
    def __init__(self):
        self.vars = []

    def setEnv(self, add):
        self.vars(add)

    def getEnvInd(self, name):
        return self.vars[name]

    def getEnv(self):
        return self.vars


def select(cp):
    env = SelEnv()
    blk = {}
    for lab, lin in cp.p.items():
        tempBlk = []
        tempLabel = XLabel(lab.interp())
        if(isinstance(lin, CBlock)):
            for l in lin.p:
                rtn = _selectT(l, env)
                if(isinstance(rtn, list)):
                    tempBlk = tempBlk + rtn
                else:
                    tempBlk.append(rtn)
        blk.update({tempLabel: XBlock([], tempBlk)})
    return XProgram(cp.info, blk)


def _selectT(cp, env):
    if isinstance(cp, CRet):
        return [XIMov(_selectA(cp.var, env), XRegister("rax")), XIRet()]
    if(isinstance(cp, CSet)):
        src = cp.exp
        dst = cp.var
        return _selectE(src, dst, env)


def _selectE(cp, dst, env):
    if(isinstance(cp, CRead)):
        return [XICall(XLabel("read_int")), XIMov(XRegister("rax"), _selectA(dst, env))]
    elif(isinstance(cp, CNeg)):
        return [XIMov(_selectA(cp.n, env), _selectA(dst, env)), XINeg(_selectA(dst, env))]
    elif(isinstance(cp, CAdd)):
        return [XIMov(_selectA(cp.l, env), _selectA(dst, env)), XIAdd(_selectA(cp.r, env), _selectA(dst, env))]
    else:
        return XIMov(_selectA(cp, env), _selectA(dst, env))


def _selectA(cp, env):
    if(isinstance(cp, CNum)):
        return XCon(cp.n)
    elif(isinstance(cp, CVar)):
        return XVar(cp.pp())


######## Uncover Live ########

def uncover_live(xp: XProgram):
    for l in xp.p.values():
        d = {}
        before = set([])
        if(isinstance(l, XBlock)):
            for i in reversed(l.blk[:-1]):
                d.update({i: before})
                #print("Live before: " + str(n) +" = " + str(before), end=' ')
                # print(w)
                # print(r)
                before = before - _uncoverW(i)
                before = before.union(_uncoverR(i))
                #print("Live after: " + str(n) +" = " + str(before) )
            # printUncover(d)
            l.aux = d
    return xp


def _uncoverW(i):
    if(isinstance(i, XINeg)):
        return _uncoverM(i.src)
    elif(isinstance(i, XIAdd)):
        return _uncoverM(i.dst)
    elif(isinstance(i, XISub)):
        return _uncoverM(i.dst)
    elif(isinstance(i, XIMov)):
        return _uncoverM(i.dst)
    elif(isinstance(i, XIPush)):
        return set([])
    elif(isinstance(i, XIPop)):
        return _uncoverM(i.src)
    return set([])


def _uncoverR(i):
    if(isinstance(i, XINeg)):
        return _uncoverM(i.src)
    elif(isinstance(i, XIAdd)):
        return _uncoverM(i.dst).union(_uncoverM(i.src))
    elif(isinstance(i, XISub)):
        return _uncoverM(i.dst).union(_uncoverM(i.src))
    elif(isinstance(i, XIMov)):
        return _uncoverM(i.src)
    elif(isinstance(i, XIPush)):
        return _uncoverM(i.src)
    elif(isinstance(i, XIPop)):
        return set([])
    return set([])


def _uncoverM(a):
    if(isinstance(a, XRegister)):
        return set([a.emit()])
    elif(isinstance(a, XVar)):
        return set([a.emit()])
    else:
        return set([])


def printUncover(uncl: dict):
    for l, afterSet in uncl.items():
        print(l.emit() + " After set: ", end="")
        for e in afterSet:
            print(e, end=" ")
        print()
    print("\n")
    return

######## Build Interferences ########


def buildInt(xp: XProgram):
    g = Graph()
    m = Graph()
    for blk in xp.p.values():
        if(isinstance(blk, XBlock)):
            for i, s in blk.aux.items():
                if(isinstance(i, XIMov)):
                    if(s):
                        d = i.dst.emit()
                        sr = i.src.emit()
                        for e in s:
                            if(not (d == e or e == sr)):
                                g.add_edge(d, str(e))
                            m.add_edge(sr, d)
                elif(isinstance(i, XIAdd)):
                    if(s):
                        d = i.dst.emit()
                        sr = i.src.emit()
                        for e in s:
                            if(not d == e):
                                g.add_edge(d, str(e))
                elif(isinstance(i, XINeg)):
                    if(s):
                        d = i.src.emit()
                        for e in s:
                            if(not d == e):
                                g.add_edge(d, str(e))
                elif(isinstance(i, XICall)):
                    if(s):
                        for e in s:
                            for u in callerSavedRegs:
                                if(not u == e):
                                    g.add_edge(u.emit(), str(e))
                else:
                    if(s):
                        d = i.dst.emit()
                        for e in s:
                            if(not d == e):
                                g.add_edge(d, str(e))
            # printGrph(g)
            # printGrph(m)
            blk.aux = (g, m)
    return xp


def printGrph(g: Graph):
    print("\n")
    for v in g:
        for w in v.get_connections():
            print("({} -> {})".format(v.get_id(), w.get_id()))


######## Color Graph ########
def saturation(v: Vertex):
    satSet = set()
    for e in v.adjacent:
        satSet.add(e.get_id())
    return satSet


def color(xp: XProgram) -> XProgram:
    for blk in xp.p.values():
        g = blk.aux[0]
        m = blk.aux[1]
        if(g.vert_dict):
            w = list(g.vert_dict.copy())
            colorList = dict()
            available = dict()
            cntr = 0

            for x in g.vert_dict:
                colorList.update({x: -1})
                available.update({cntr: False})
                cntr += 1
            colorList[w[0]] = 0

            while w:
                u = w[0]
                color = 0
                mvadj = None
                adj = saturation(g.vert_dict[u])
                if(u in m.vert_dict):
                    mvadj = saturation(m.vert_dict[u])
                for e in adj:
                    if(e in colorList and colorList[e] != -1):
                        available[colorList[e]] = True

                if(mvadj):
                    for e in mvadj:
                        if(e in colorList and colorList[e] != -1):
                            available[colorList[e]] = True

                for e in available:
                    if(available[e] == False):
                        color = e
                        break

                colorList[u] = color

                for e in adj:
                    if(e in colorList and colorList[e] != -1):
                        available[colorList[e]] = False

                w.remove(u)

            regColorList = dict(enumerate(usableRegs))
            # print(colorList)
            # print(regColorList)
            maxKey = max([int(s) for s in colorList.values()])
            ss = 0
            # print(maxKey)
            if(maxKey > len(regColorList)):
                stackSize = maxKey
                i = len(regColorList)

                while(i <= stackSize):
                    regColorList.update({i: XMem(XRegister("rbp"), cntr)})
                    ss += 8
                    i += 1
                ss = cntr + 8
                if(not ss % 2 == 0):
                    ss += 1
            for v, c in colorList.items():
                colorList.update({v: regColorList[c]})
            blk.aux = (colorList, ss)
            # print(colorList)
        else:
            blk.aux = ({}, 0)
    return xp


################ Allocate Registers ################

def allocate_registers(xp: XProgram) -> XProgram:
    newXp = color(xp)
    # Gets whatever is the first block in program assumes it is main
    # Because Xprogram should only have one block to start
    firstBlock: XBlock = list(newXp.p.values())[0]
    colorList, stackSize = firstBlock.aux
    print(newXp.emit())
    print(colorList)
    print(stackSize)
    newXp = assign_register(newXp, colorList)
    newXp = mainpass(newXp, stackSize)
    return newXp

################ Assign Registers ################


def assign_register(xp: XProgram, regs: dict) -> XProgram:
    originalMain = []
    body = []
    for lab, blk in xp.p.items():
        if(lab.emit() == "main"):
            if(isinstance(blk, XBlock)):
                originalMain = blk.blk

    for instr in originalMain:
        body.append(_assign(instr, regs))
    body = body[:-1]

    body.append(XIJmp(XLabel("end")))
    bdy = {XLabel("body"): XBlock([], body)}

    progm = {}
    progm.update(bdy)
    return XProgram(xp.info, progm)


def _assign(xp, regs):
    if(isinstance(xp, XIAdd)):
        return XIAdd(_assignA(xp.src,  regs), _assignA(xp.dst,  regs))
    elif(isinstance(xp, XISub)):
        return XISub(_assignA(xp.src, regs), _assignA(xp.dst,  regs))
    elif(isinstance(xp, XIMov)):
        return XIMov(_assignA(xp.src,  regs), _assignA(xp.dst, regs))
    elif(isinstance(xp, XINeg)):
        return XINeg(_assignA(xp.src,  regs))
    elif(isinstance(xp, XIPush)):
        return XIPush(_assignA(xp.src,  regs))
    elif(isinstance(xp, XIPop)):
        return XIPush(_assignA(xp.src, regs))
    else:
        return xp


def _assignA(a, v):
    if(isinstance(a, XVar)):
        if(a.emit() in v):
            return v[a.emit()]
        return XRegister("rax")
    else:
        return a


######## Main Pass ########

def mainpass(xp: XProgram, alloc: int):
    mainBdy = [XIPush(XRegister("rbp")), XIMov(
        XRegister("rsp"), XRegister("rbp")), XIPush(XRegister("rbx"))]
    endBlk = [XIAdd(XCon(alloc), XRegister("rsp")), XIPop(
        XRegister("rbx")), XIPop(XRegister("rbp"))]

    for r in calleeSavedRegs:
        mainBdy.append(XIPush(r))
        endBlk.append(XIPop(r))
    mainBdy = mainBdy + \
        [XISub(XCon(alloc), XRegister("rsp")), XIJmp(XLabel("body"))]
    endBlk = endBlk + [XIMov(XRegister("rax"), XRegister("rdi")),
                       XICall(XLabel("print_int")), XIRet()]

    main = {XLabel("main"): XBlock([], mainBdy)}
    end = {XLabel("end"): XBlock([], endBlk)}
    xp.p.update(main)
    xp.p.update(end)

    return XProgram(xp.info, xp.p)


######## Patch Instr ########


def patch(xp):
    if(isinstance(xp, XProgram)):
        progs = xp.p
        newP = {}
        for lab, blks in progs.items():
            if(isinstance(blks, XBlock)):
                newBlks = []
                for i in blks.blk:
                    newBlks = newBlks + _patch(i)
                newP.update({lab: XBlock([], newBlks)})
        return XProgram(xp.info, newP)


def _patch(i):
    if(isinstance(i, XIAdd)):
        if(isinstance(i.src, XMem) and isinstance(i.dst, XMem)):
            return [XIMov(i.src, XRegister("rax")), XIAdd(XRegister("rax"), i.dst)]
    elif(isinstance(i, XISub)):
        if(isinstance(i.src, XMem) and isinstance(i.dst, XMem)):
            return [XIMov(i.src, XRegister("rax")), XISub(XRegister("rax"), i.dst)]
    elif(isinstance(i, XIMov)):
        if(i.dst.emit() == i.src.emit()):
            return []
        if(isinstance(i.src, XMem) and isinstance(i.dst, XMem)):
            return [XIMov(i.src, XRegister("rax")), XIMov(XRegister("rax"), i.dst)]
    return [i]
