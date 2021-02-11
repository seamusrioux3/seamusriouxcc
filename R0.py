import random
from datetime import datetime

# R0 Data types

class REnv:
    def __init__(self):
        self.env ={}
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


class RNegate:
    def __init__(self, _num):
        self.num = _num

    def pp(self):
        return "-(" + str(self.num.pp()) + ")"

    def interp(self, e=None):
        return -1*self.num.interp(e)


class RAdd:
    def __init__(self, _left, _right):
        self.left = _left
        self.right = _right

    def pp(self):
        return "(+ " + self.left.pp() + " " + self.right.pp() + ")"

    def interp(self, e=None):
        return self.left.interp(e) + self.right.interp(e)


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


class Pow:
    def __init__(self, _num):
        self.num = _num

    def pp(self):
        return "2^" + str(self.num.pp())

    def interp(self, e =None):
        if(self.num.interp() == 0):
            return 1
        else:
            return RAdd(Pow(RNum(self.num.interp()-1)), Pow(RNum(self.num.interp()-1))).interp(e)

# R1 data types


class RVar:
    def __init__(self, _name):
        self.name = _name

    def pp(self):
        return str(self.name)

    def interp(self, e=None):
        if(e.getEnv()[self.name]):
            return e.getEnv()[self.name]
        return "ERROR"


class RLet:
    def __init__(self, _var, _l, _r):
        self.var = _var
        self.l = _l
        self.r = _r

    def pp(self):
        return "Let " + self.var.pp() + " = " + self.l.pp() + " in " + self.r.pp()

    def interp(self, e = None):
        if(not e):
            e = REnv()
        e.setEnv(self.var.name, self.l.interp(e))
        return self.r.interp(e)


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

class UNEnv:
    def __init__(self):
        self.varCntr =0
        self.env ={}
def uniquify(e):
    env = UNEnv()
    e = uni(e, env)
    return e

def uni(e = None, uenv = UNEnv()):
    if(isinstance(e,RNum)):
        return e
    elif(isinstance(e,RRead)):
        return e
    elif(isinstance(e, RNegate)):
        return RNegate(uni(e.num, uenv))
    elif(isinstance(e, RAdd)):
        return RAdd(uni(e.left, uenv), uni(e.right, uenv))
    elif(isinstance(e, RVar)):
        if e.pp() in uenv.env:
            return RVar(uenv.env[e.pp()])
        else:
            print("VAR UNBOUND")
            return "FAILURE"
    elif(isinstance(e,RLet)):
         uenv.varCntr+=1
         x = RVar("V"+str(uenv.varCntr))
         l = uni(e.l,uenv)
         uenv.env[e.var.pp()] = x.pp()
         r = uni(e.r,uenv)
         return RLet(x,l,r)
         
    return 0

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
        print(env.cntr)
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

###### C0 Program Data Types ########

class CProgram:
    def __init__(self, _p):
        self.p = _p

    def pp(self):
        return "".join([i.pp() + "\n"+ "\n".join([l.pp() for l in j])\
             for i,j in self.p.items()])
    
    def interp(self):
        tempBlks = {}
        for i,j in self.p.items():
            tempBlks.update({i.interp():j})
        #print(tempBlks)
        env = CEnv()
        env.setBlk(tempBlks)
        rtn = 0
        for i in env.blk["main"]:
            rtn = i.interp(env)
        return rtn

class CEnv:
    def __init__(self):
        self.var = {}
        self.blk = {}
        self.cntr = 0
    
    def setBlk(self,add):
        self.blk.update(add)
        
    def setVar(self,add):
        self.var.update(add)

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
        return "return "+ self.var.pp()
    
    def interp(self,env):
        return env.var[self.var.pp()]

class CNum:
    def __init__(self, _n):
        self.n = _n

    def pp(self):
        return str(self.n) 
    
    def interp(self,env):
        return self.n

class CVar:
    def __init__(self, _var):
        self.var = _var
    
    def pp(self):
        return self.var
    
    def interp(self,env):
        return env.var[self.var]

class CRead:
    def __init__(self):
        self.r = 0
    
    def pp(self):
        return "Read"
    
    def interp(self,env):
        env.cntr +=1
        return env.cntr

class CNeg:
    def __init__(self, _n):
        self.n = _n 
    
    def pp(self):
        return "-("+self.n.pp() +")"
    
    def interp(self,env):
        return -1* self.n.interp(env)

class CAdd:
    def __init__(self, _l, _r):
        self.l = _l
        self.r = _r
    
    def pp(self):
        return "(+ " + self.l.pp() + " " + self.r.pp() +")"
    
    def interp(self,env):
        return self.l.interp(env) + self.r.interp(env)

class CSet:
    def __init__(self, _var, _exp):
        self.var = _var
        self.exp = _exp
    
    def pp(self):
        return "(set! " + self.var.pp() + " " + self.exp.pp() + ")"
    
    def interp(self,env):
        env.setVar({self.var.pp():self.exp.interp(env)})
        return 0
