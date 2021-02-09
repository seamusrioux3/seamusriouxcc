import random
from datetime import datetime

# R0 Data types


class RNum:
    def __init__(self, _num):
        self.num = _num

    def pp(self):
        return str(self.num)

    def interp(self, e=None):
        return self.num


class RNegate:
    def __init__(self, _num):
        self.num = _num

    def pp(self):
        return "-(" + str(self.num.pp()) + ")"

    def interp(self, e=None):
        if(e):
            return -1*self.num.interp(e)
        return -1*self.num.interp()


class RAdd:
    def __init__(self, _left, _right):
        self.left = _left
        self.right = _right

    def pp(self):
        return "(+ " + self.left.pp() + " " + self.right.pp() + ")"

    def interp(self, e=None):
        if(e):
            return self.left.interp(e) + self.right.interp(e)
        else:
            return self.left.interp() + self.right.interp()


class RRead:
    def __init__(self):
        self.num = 0

    def pp(self):
        return "Read"

    def interp(self,  e=None):
        inp = input("Read: ")
        if(inp == ""):
            self.num = 1
        else:
            self.num = int(inp)
        return self.num


class Pow:
    def __init__(self, _num):
        self.num = _num

    def pp(self):
        return "2^" + str(self.num.pp())

    def interp(self):
        if(self.num.interp() == 0):
            return 1
        else:
            return RAdd(Pow(RNum(self.num.interp()-1)), Pow(RNum(self.num.interp()-1))).interp()

# R1 data types


class RVar:
    def __init__(self, _name):
        self.name = _name

    def pp(self):
        return str(self.name)

    def interp(self, e=None):
        if(e[self.name]):
            return e[self.name].interp(e)
        return "ERROR"


class RLet:
    def __init__(self, _var, _l, _r):
        self.var = _var
        self.l = _l
        self.r = _r

    def pp(self):
        return "Let " + self.var.pp() + " = " + self.l.pp() + " in " + self.r.pp()

    def interp(self, e=None):
        if(e):
            e[self.var.name] = self.l
            return self.r.interp(e)
        else:
            env = {}
            env[self.var.name] = self.l
            return self.r.interp(env)


# Functions
def randomR0(n):
    random.seed(datetime.now())
    ret = 0
    if(n == 0):
        ret = random.choice([RNum(random.randint(0, 16)), RRead()])
    else:
        ret = random.choice(
            [RAdd(randomR0(n-1), randomR0(n-1)), RNegate(randomR0(n-1))])
    return ret


def randomR1(n, v):
    random.seed(datetime.now())
    ret = 0
    if(n == 0):
        if(v):
            chosenVar = random.choice(v)
            ret = random.choice(
                [RNum(random.randint(0, 16)), chosenVar, RRead()])
        else:
            ret = random.choice([RNum(random.randint(0, 16)), RRead()])
    else:
        newVar = RVar("V" + str(len(v)))
        ret = random.choice([RAdd(randomR1(n-1, v), randomR1(n-1, v)), RNegate(
            randomR1(n-1, v)), RLet(newVar, randomR1(n-1, v), randomR1(n-1, v+[newVar]))])
    return ret


def optimizer(n, env=None):
    if isinstance(n, RNum):
        return n
    elif isinstance(n, RRead):
        return n
    elif isinstance(n, RNegate):
        e = n.num
        if(isinstance(e, RNum)):
            return RNum(-1 * e.interp(env))
        elif(isinstance(e, RNegate)):
            return optimizer(e, env)
        elif(isinstance(e, RAdd)):
            if(isinstance(e.left, RNum)):
                return RAdd(RNum(-1*e.left.interp()), RNegate(optimizer(e.right)))
            else:
                return RNegate(optimizer(e, env))
        elif(isinstance(e, RVar)):
            return RNegate(optimizer(e, env))
        else:
            return n
    elif isinstance(n, RAdd):
        l = n.left
        r = n.right
        if(isinstance(l, RNum) and isinstance(r, RNum)):
            return RNum(l.interp(env) + r.interp(env))

        elif(isinstance(l, RNum) and isinstance(r, RAdd) and isinstance(r.left, RNum)):
            return RAdd(RNum(l.interp(env) + r.left.interp(env)), r.right)

        elif(isinstance(l, RAdd) and isinstance(r, RNum) and isinstance(r.right, RNum)):
            return RAdd(RNum(l.interp(env) + r.right.interp(env)), r.left)

        elif(isinstance(l, RAdd) and isinstance(l.left, RNum) and isinstance(r, RAdd) and isinstance(r.left, RNum)):
            return RAdd(RNum(l.left.interp(env) + r.left.interp(env)), RAdd(l.left, r.left))
        elif(not isinstance(l, RNum) and isinstance(r, RNum)):
            return optimizer(RAdd(r, l), env)
        else:
            return RAdd(optimizer(l, env), optimizer(r, env))
    elif(isinstance(n, RVar)):
        if(env):
            if(env[n.name]):
                return env[n.name]
            else:
                print("ERROR UNBOUND VAR")
                return n
    elif(isinstance(n, RLet)):
        xe = optimizer(n.l)
        if(isinstance(xe, RNum)):
            if(env):
                env[n.var.name] = xe
            else:
                env = {}
                env[n.var.name] = xe
            be = optimizer(n.r, env)
            return be
        else:
            if(env):
                env[n.var.name] = xe
            else:
                env = {}
                env[n.var.name] = xe
            be = optimizer(n.r, env)

        return RLet(n.var, xe, be)


############ X0 Programs ############

class XEnv:
    def __init__(self):
        self.reg = {}
        self.var = {}
        self.mem = {}
        self.blk = {}
        self.cntr =0


class XProgram:
    def __init__(self, _p):
        self.p = _p

    def emit(self):
        return ".global main\n\n" + "".join(["\n"+x.emit() + ":\n" + y.emit() for x, y in self.p])

    def interp(self):
        env = XEnv()
        for a, b in self.p:
            env.blk[a.interp(env)] = b
        env = env.blk["main"].interp(env)
        print(env.reg)
        print(env.var)
        print(env.mem)
        print(env.blk)
        return env.reg["RAX"]


class XBlock:
    def __init__(self, _blk):
        self.blk = _blk

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
        return self.reg.emit() + " (" + str(self.num) + ")"

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
        env = self.dst.set(env, self.src.interp(env) - self.dst.interp(env))
        return env


class XISub:
    def __init__(self, _src, _dst):
        self.src = _src
        self.dst = _dst

    def emit(self):
        return "subq" + " " + self.src.emit() + ", " + self.dst.emit()

    def interp(self, env):
        env = self.dst.set(env, self.src.interp(env) - self.dst.interp(env))
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
            env.cntr = env.cntr+1
            XIMov(XCon(env.cntr),XRegister("RAX")).interp(env)
        else:
            env = env.blk[temp].interp(env)
        return env


class XIJmp:
    def __init__(self, _src):
        self.src = _src

    def emit(self):
        return "jmp" + " " + self.src.emit()

    def interp(self, env):
        env = env.blk[self.src.interp(env)].interp(env)
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
