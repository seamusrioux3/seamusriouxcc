import random
from datetime import datetime
from graph import Vertex, Graph
# R0 Data types
freeptr = 0
fromend = 9999
wordsize = 8

class REnv:
    def __init__(self):
        self.env = {"free_ptr":RNum(0), "from_end":RNum(1024*1024*1024)}
        self.type = {}

    def getEnv(self):
        return self.env

    def setEnv(self, left, right):
        self.env[left] = right


class RNum:
    def __init__(self, _num):
        self.num = _num
        self.has_type = "NUM"

    def pp(self):
        return str(self.num)

    def tp(self):
        return "RNum("+str(self.num) + ")"

    def interp(self, e=None):
        return self.num

    def typec(self, env=None):
        return self.has_type


class RNegate:
    def __init__(self, _num):
        self.num = _num
        self.has_type = "NUM"

    def pp(self):
        return "-(" + str(self.num.pp()) + ")"

    def tp(self):
        return "RNegate("+self.num.tp() + ")"

    def interp(self, e=None):
        return -1*self.num.interp(e)

    def typec(self, env=None):
        if(self.has_type == "NUM"):
            return "NUM"
        return "ERROR"


class RAdd:
    def __init__(self, _left, _right):
        self.left = _left
        self.right = _right
        self.has_type = "NUM"

    def pp(self):
        return "(+ " + self.left.pp() + " " + self.right.pp() + ")"

    def tp(self):
        return "RAdd( " + self.left.tp() + ", " + self.right.tp() + ")"

    def interp(self, e=None):
        if(not e):
            e = REnv()
        li = self.left.interp(e)
        return li + self.right.interp(e)

    def typec(self, env=None):
        if(self.left.typec(env) == self.right.typec(env) == self.has_type):
            return self.has_type
        return "ERROR"


class RRead:
    def __init__(self):
        self.num = 0
        self.has_type = "NUM"

    def pp(self):
        return "Read"

    def tp(self):
        return "RRead()"

    def interp(self,  e=None):
        return 1
        inp = input("Read: ")
        if(inp == ""):
            self.num = 1
        else:
            self.num = int(inp)
        return self.num

    def typec(self, env=None):
        return self.has_type


###### R1 data types ######


class RVar:
    def __init__(self, _name):
        self.name = _name

    def pp(self):
        return str(self.name)

    def tp(self):
        return "RVar(" + "\""+str(self.name)+"\""+")"

    def interp(self, e=None):
        if(self.name in e.getEnv()):
            value = e.getEnv()[self.name]
            return value.interp(e)
        return "ERROR"

    def typec(self, env=None):
        if(self.name in env.getEnv()):
            return env.type[self.name]
        return "ERROR"


class RLet:
    def __init__(self, _var, _l, _r):
        self.var = _var
        self.l = _l
        self.r = _r
        self.has_type = "NUM"

    def pp(self):
        return "Let " + self.var.pp() + " = " + self.l.pp() + " in \n" + self.r.pp()

    def tp(self):
        return "RLet(" + self.var.tp() + ", " + self.l.tp() + ", " + self.r.tp() + ")"

    def interp(self, e=None):
        if(not e):
            e = REnv()
        self.l.interp(e)
        e.setEnv(self.var.name, self.l)
        return self.r.interp(e)

    def typec(self, env=None):
        if(not env):
            env = REnv()
        env.type.update({self.var.name: self.l.typec(env)})
        env.setEnv(self.var.name, self.l.interp(env))
        if(self.l.typec(env) == self.r.typec(env) or self.r.typec(env) == "VECTOR" or self.l.typec(env) == "VECTOR"):
            rt = self.r.typec(env)
            self.has_type = rt
            return rt
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
        self.has_type = "BOOL"

    def pp(self):
        return "(" + self.op + " " + self.l.pp() + " " + self.r.pp() + ")"

    def tp(self):
        return "RCmp(" + "\"" + self.op + "\"" + ", " + self.l.tp() + ", " + self.r.tp() + ")"

    def interp(self, env=None):
        if(not env):
            env = REnv()
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
        self.has_type = "BOOL"

    def pp(self):
        return "(if " + self.var.pp() + " " + self.l.pp() + " " + self.r.pp() + ")"

    def tp(self):
        return "RIf(" + self.var.tp() + ", " + self.l.tp() + ", " + self.r.tp() + ")"

    def interp(self, env=None):
        if(not env):
            env = REnv()
        v = self.var.interp(env)
        l = self.l.interp(env)
        r = self.r.interp(env)
        return l if v else r

    def typec(self, env=None):
        if(not env):
            env = REnv()
        v = self.var.typec(env)
        v = self.var.interp(env)
        lt = self.l.typec(env)
        rt = self.r.typec(env)
        if(v):
            self.has_type = lt
            return lt
        else:
            self.has_type = rt
            return rt


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
        self.has_type = "BOOL"

    def pp(self):
        return str(self.b)

    def tp(self):
        return "RBool("+str(self.b) + ")"

    def interp(self, env=None):
        return self.b

    def typec(self, env=None):
        return self.has_type


############ R3 Programs ############
class RUnit:
    def pp(self):
        return "Unit"

    def tp(self):
        return "RUnit()"

    def typec(self, env = None):
        return "Unit"

    def interp(self, env=None):
        return "Unit"


class RVector:
    def __init__(self, args):
        self.args = args
        self.has_type = "VECTOR"

    def pp(self):
        out = "Vector("
        for a in self.args:
            out += a.pp() + " "
        out = out[:-1]
        return out + ")"

    def tp(self):
        out = "RVector(["
        for a in self.args:
            out += a.tp() + ", "
        out = out[:-2]
        return out + "])"

    def interp(self, env):
        return self

    def typec(self, env=None):
        intp = "VECTOR"
        # for i in self.args:
        #     temp = i.typec(env)
        #     if(intp == "VECTOR"):
        #         intp = temp
        #     elif(not temp == intp):
        #         return "VECTOR"
        # self.has_type = intp
        return intp


class RVectorRef:
    def __init__(self, _exp, _ref):
        self.exp = _exp
        self.ref = _ref

    def pp(self):
        return "vector-ref " + self.exp.pp() + " " + self.ref.pp()

    def tp(self):
        return "RVectorRef(" + self.exp.tp() + ", " + self.ref.tp() + ")"

    def interp(self, env: REnv):
        vec = self.exp.interp(env)
        if(isinstance(vec, RVector)):
            return vec.args[self.ref.interp(env)].interp(env)
        elif(isinstance(vec, RAllocate)):
            return vec.vec.arg[self.ref.interp(env)].interp(env)

    def typec(self, env: REnv):
        vec = self.exp.interp(env)
        if(isinstance(vec, RVector)):
            return vec.args[self.ref.interp(env)].typec(env)


class RVectorSet:
    def __init__(self, _exp, _ref, _var):
        self.exp = _exp
        self.ref = _ref
        self.var = _var

    def pp(self):
        return "vector-set!" + " " + self.exp.pp() + " " + self.ref.pp() + " " + self.var.pp()

    def tp(self):
        return "RVectorSet( " + self.exp.tp() + ", " + self.ref.tp() + ", " + self.var.tp() + ")"

    def interp(self, env: REnv):
        vec = self.exp.interp(env)
        if(isinstance(vec, RVector)):
            self.var.interp(env)
            vec.args[self.ref.interp(env)] = self.var
        elif(isinstance(vec, RAllocate)):
            self.var.interp(env)
            vec.vec.arg[self.ref.interp(env)] = self.var
        return self

    def typec(self, env: REnv):
        return self.var.typec(env)


class RAllocate:
    def __init__(self, _num, _ty):
        self.num = _num
        self.has_type = _ty
        arr = [0 for i in range(0, _num.interp())]
        self.vec = RVector(arr)

    def pp(self):
        return "Allocate(" + self.num.pp() + ", " + self.has_type + ")"

    def tp(self):
        return "RAllocate(" + self.num.tp() + ", " + "\"" + self.has_type + "\"" + ")"

    def interp(self, env: REnv):
        return self.vec

    def typec(self, env: REnv):
        return self.var.typec(env)


class RCollect():
    def __init__(self, _num):
        self.num = _num

    def pp(self):
        return "Collect(" + self.num.pp() + ")"

    def tp(self):
        return "RCollect(" + self.num.tp() + ")"

    def interp(self, env=None):
        return self.num.interp(env)


class RGlobal:
    def __init__(self, _name):
        self.name = _name

    def pp(self):
        return "Global " + str(self.name)

    def tp(self):
        return "RGlobal(" + "\""+str(self.name)+"\""+")"

    def interp(self, e=None):
        if(self.name in e.getEnv()):
            value = e.getEnv()[self.name]
            return value.interp(e)
        return "ERROR"

    def typec(self, env=None):
        if(self.name in env.getEnv()):
            return env.type[self.name]
        return "ERROR"


############ X0 Programs ############


class XEnv:
    def __init__(self):
        self.curlab = ""
        self.reg = {}
        self.var = {"free_ptr":0, "from_end":1024*1024*1024}
        self.mem = {}
        self.blk = {}
        self.cmp = []
        self.cntr = 0


class XProgram:
    def __init__(self, _globals, _info, _p):
        self.p = _p
        self.info = _info
        self.globals = _globals

    def emit(self):
        return ".global main\n" + "".join([".global " + d.emit() + "\n" for d in self.globals]) + "".join(["\n"+x.emit() + ":" + "\n" + y.emit() for x, y in self.p.items()])

    def interp(self):
        env = XEnv()
        for a, b in self.p.items():
            env.blk[a.interp(env)] = XBlock(None, list(b.blk))
        if("main" in env.blk):
            env.curlab = "main"
            env.blk["main"].interp(env)
        else:
            env.curlab = next(iter(env.blk))
            env.blk[next(iter(env.blk))].interp(env)
        print(env.reg)
        print(env.var)
        print(env.mem)
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
            if(isinstance(a, XIRet)):
                break
            else:
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
        if(isinstance(env.var[self.name], int)):
            return env.var[self.name]
        else:
            return env.var[self.name].interp(env)

    def set(self, env, val):
        env.var[self.name] = val

    def getName(self):
        return self.name


class XRegister:
    def __init__(self, _register):
        ######## Register must be strictly these ########
        if(_register.lower() in ["rsp", "rbp", "rax", "rbx", "rcx", "rdx", "rsi", "rdi", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15", "rip"]):
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
               XRegister("r8"), XRegister("r9"), XRegister("r13"),
              XRegister("r14"), XRegister("r15")]
tempReg = XRegister("r10")
tempReg2 = XRegister("r11")
root_stack_reg = XRegister("r12")


class XCon:
    def __init__(self, _value):
        self.value = _value

    def emit(self):
        return "$" + str(self.value)

    def interp(self, env):
        return self.value

class XGlobal:
    def __init__(self, _var):
        self.var = _var

    def set(self, env, val):
        env.var[self.var] = val

    def emit(self):
        return self.var

    def interp(self, env: XEnv):
        if(isinstance(env.var[self.var], int)):
            return env.var[self.var]
        else:
            return env.var[self.var].interp(env)

    def getName(self):
        return self.name

class XMem:
    def __init__(self, _reg, _num):
        self.reg = _reg
        self.num = _num

    def emit(self):
        if(isinstance(self.num, XGlobal)):
            return self.num.emit() + "(" + str(self.reg.emit()) + ")"
        return str(self.num) + "(" + str(self.reg.emit()) + ")"

    def interp(self, env):
        if(isinstance(self.num, XGlobal)):
            if(self.reg.interp(env) + self.num.interp(env) in env.mem.keys()):
                return env.mem[self.reg.interp(env) + self.num.interp(env)]
            else:
                env.mem[self.reg.interp(env) + self.num.interp(env)] = 0
                return env.mem[self.reg.interp(env) + self.num.interp(env)]
        else:
            if(self.reg.interp(env) + self.num in env.mem.keys()):
                return env.mem[self.reg.interp(env) + self.num]
            else:
                env.mem[self.reg.interp(env) + self.num] = 0
                return env.mem[self.reg.interp(env) + self.num]

    def set(self, env, val):
        if(isinstance(self.num, XGlobal)):
            env.mem[self.reg.interp(env) + self.num.interp(env)] = val
        else:
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


class XICMov:
    def __init__(self, _cc, _src, _dst):
        self.src = _src
        self.dst = _dst
        self.cc = _cc

    def emit(self):
        return "cmov" + self.cc.emit() + " " + self.src.emit() + ", " + self.dst.emit()

    def interp(self, env):
        camp = env.cmp.pop()
        if(getTrueCmp(self.cc, camp[0].interp(env), camp[1].interp(env))):
            env = self.dst.set(env, self.src.interp(env))
            # tem = env.curlab
            # #print(tem)
            # env.curlab = self.label.interp(env)
            # a = env.blk[tem].blk.index(self)
            # #print(str(a))
            # env.blk[tem].blk.remove(env.blk[tem].blk[a+1])
            # env = env.blk[self.label.emit()].interp(env)
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
        elif(temp == "collect"):
            pass
        elif(temp == "init_mem"):
            pass
        elif(temp == "print_value"):
            pass
        else:
            tem = env.curlab
            env.curlab = temp
            env.blk[temp].interp(env)
            env.curlab = tem
        return env


class XIJmp:
    def __init__(self, _src):
        self.src = _src

    def emit(self):
        return "jmp" + " " + self.src.emit()

    def interp(self, env):
        tem = env.curlab
        env.curlab = self.src.interp(env)
        env.blk[self.src.interp(env)].interp(env)
        env.curlab = tem
        return env


class XIPush:
    def __init__(self, _src):
        self.src = _src

    def emit(self):
        return "pushq" + " " + self.src.emit()

    def interp(self, env):
        XISub(XCon(8), XRegister("rsp")).interp(env)
        XIMov(self.src, XMem(XRegister("rsp"), 0)).interp(env)
        return env


class XIPop:
    def __init__(self, _src):
        self.src = _src

    def emit(self):
        return "popq" + " " + self.src.emit()

    def interp(self, env):
        XIMov(XMem(XRegister("rsp"), 0), self.src).interp(env)
        XIAdd(XCon(8), XRegister("rsp")).interp(env)
        return env

###### X1 Program Data Types ########



class XByteRegister:
    def __init__(self, _r):
        self.r = _r

    def emit(self):
        return "%" + self.r

    def interp(self, env):
        if(self.r in env.reg.keys()):
            return env.reg[self.r]
        else:
            env.reg[self.r] = 0
            return env.reg[self.r]

    def set(self, env, val):
        env.reg[self.r] = val

    def getName(self):
        return self.r


class XEq:
    def __init__(self):
        self.c = "e"
        self.l = 0
        self.r = 0

    def emit(self):
        return self.c


class XLEq:
    def __init__(self):
        self.c = "le"
        self.l = 0
        self.r = 0

    def emit(self):
        return self.c


class XL:
    def __init__(self):
        self.c = "l"
        self.l = 0
        self.r = 0

    def emit(self):
        return self.c


class XGEq:
    def __init__(self):
        self.c = "ge"
        self.l = 0
        self.r = 0

    def emit(self):
        return self.c


class XG:
    def __init__(self):
        self.c = "g"
        self.l = 0
        self.r = 0

    def emit(self):
        return self.c


class XIXor:
    def __init__(self, _l, _r):
        self.l = _l
        self.r = _r

    def emit(self):
        return "xorq" + " " + self.l.emit() + ", " + self.r.emit()

    def interp(self, env):
        env = self.r.set(env, self.l.interp(env) ^ self.r.interp(env))
        return env


class XICmp:
    def __init__(self, _l, _r):
        self.l = _l
        self.r = _r

    def emit(self):
        return "cmpq" + " " + self.r.emit() + ", " + self.l.emit()

    def interp(self, env):
        env.cmp.append([self.l, self.r])


class XISet:
    def __init__(self, _cc, _arg):
        self.cc = _cc
        self.arg = _arg

    def emit(self):
        return "set" + self.cc.emit() + " " + self.arg.emit()

    def interp(self, env=XEnv()):
        c = env.cmp.pop(0)
        c = getTrueCmp(self.cc, c[0].interp(env), c[1].interp(env))
        env = self.arg.set(env, c)
        return env


class XIMovzb:
    def __init__(self, _l, _r):
        self.l = _l
        self.r = _r

    def emit(self):
        return "movzbq" + " " + self.l.emit() + ", " + self.r.emit()

    def interp(self, env):
        env = self.r.set(env, self.l.interp(env))
        return env


class XIJmpIf:
    def __init__(self, _cc, _label):
        self.cc = _cc
        self.label = _label

    def emit(self):
        return "j" + self.cc.emit() + " " + self.label.emit()

    def interp(self, env):
        camp = env.cmp.pop()
        if(getTrueCmp(self.cc, camp[0].interp(env), camp[1].interp(env))):
            tem = env.curlab
            # print(tem)
            env.curlab = self.label.interp(env)
            a = env.blk[tem].blk.index(self)
            # print(str(a))
            env.blk[tem].blk.remove(env.blk[tem].blk[a+1])
            env = env.blk[self.label.emit()].interp(env)
        return env


def getTrueCmp(cc, l, r):
    if(isinstance(cc, XGEq)):
        return l >= r
    elif(isinstance(cc, XG)):
        return l > r
    elif(isinstance(cc, XLEq)):
        return l <= r
    elif(isinstance(cc, XL)):
        return l < r
    elif(isinstance(cc, XEq)):
        return l == r


########### X2 Datatypes ###########
class XILeaq:
    def __init__(self, _src, _dst):
        self.src = _src
        self.dst = _dst
        self.has_type = "NUM"

    def emit(self):
        return "leaq " + self.src.emit() + " " + self.dst.emit()

    def interp(self, env):
        env = self.dst.set(env, self.src.interp(env))
        return env


class XType:
    def __init__(self, _t):
        self.t = _t

    def emit(self):
        return self.t
    
    def interp(self, env):
        #if(self.t == "VECTOR"):
        return 3
        #return self

###### C0 Program Data Types ########


class CEnv:
    def __init__(self):
        self.var = {"free_ptr":0, "from_end":1024*1024*1024}
        self.blk = {}
        self.type = {}
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
        return "".join(["\n\n" + l.pp() + ":" + b.pp() for l, b in self.p.items()])

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
        self.has_type = "NUM"

    def pp(self):
        return str(self.n)

    def typec(self, env=None):
        return self.has_type

    def interp(self, env):
        return self.n


class CVar:
    def __init__(self, _var):
        self.var = _var

    def pp(self):
        return self.var

    def typec(self, env=None):
        if(self.var in env.type):
            return env.type[self.var]
        return "ERROR"

    def interp(self, env):
        return env.var[self.var]


class CRead:
    def __init__(self):
        self.r = 0
        self.has_type = "NUM"

    def pp(self):
        return "Read"

    def typec(self, env=None):
        return self.has_type

    def interp(self, env):
        return 1
        env.cntr += 1
        return env.cntr


class CNeg:
    def __init__(self, _n):
        self.n = _n
        self.has_type = "NUM"

    def pp(self):
        return "-("+self.n.pp() + ")"

    def typec(self, env=None):
        temp = self.n.typec(env)
        if(temp != "NUM"):
            self.has_type = "ERROR"
        else:
            self.has_type = "NUM"
        return self.has_type

    def interp(self, env):
        return -1 * self.n.interp(env)


class CAdd:
    def __init__(self, _l, _r):
        self.l = _l
        self.r = _r
        self.has_type = "NUM"

    def pp(self):
        return "(+ " + self.l.pp() + " " + self.r.pp() + ")"

    def typec(self, env=None):
        tempL = self.l.typec(env)
        tempR = self.r.typec(env)
        if(tempL != "NUM" or tempR != "NUM"):
            self.has_type = "ERROR"
        else:
            self.has_type = "NUM"
        return self.has_type

    def interp(self, env):
        return self.l.interp(env) + self.r.interp(env)


class CSet:
    def __init__(self, _var, _exp):
        self.var = _var
        self.exp = _exp

    def pp(self):
        return "(set! " + self.var.pp() + " " + self.exp.pp() + ")"

    def typec(self, env=None):
        tempE = self.exp.typec(env)
        env.type[self.var.pp()] = tempE
        return tempE

    def interp(self, env):
        env.setVar({self.var.pp(): self.exp.interp(env)})
        return 0


###### C1 Program Data Types ########


class CBool:
    def __init__(self, _b):
        self.b = _b
        self.has_type = "BOOL"

    def pp(self):
        return str(self.b)

    def typec(self, env=None):
        return self.has_type

    def interp(self, env):
        return self.b


class CCmp:
    def __init__(self, _op, _l, _r):
        self.op = _op
        self.l = _l
        self.r = _r
        self.has_type = "BOOL"

    def pp(self):
        return "(" + self.op + " " + self.l.pp() + " " + self.r.pp() + ")"

    def typec(self, env=None):
        return self.has_type

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


class CSetCC:
    def __init__(self, _cmp, _var, _t, _f):
        self.cmp = _cmp
        self.var = _var
        self.t = _t
        self.f = _f

    def pp(self):
        return "(setc! " + self.cmp.pp() + " " + self.var.pp() + " " + self.t.pp() + " " + self.f.pp() + ")"

    def interp(self, env):
        if(self.cmp.interp(env)):
            env.setVar({self.var.pp(): self.t.interp(env)})
        else:
            env.setVar({self.var.pp(): self.f.interp(env)})
        return 0


class CNot:
    def __init__(self, _e):
        self.e = _e
        self.has_type = "BOOL"

    def pp(self):
        return "not(" + self.e.pp() + ")"

    def typec(self, env=None):
        temp = self.e.typec(env)
        if(temp != "BOOL"):
            self.has_type = "ERROR"
        else:
            self.has_type = "BOOL"
        return self.has_type

    def interp(self, env):
        return not self.e.interp(env)


class CGoto:
    def __init__(self, _label):
        self.label = _label

    def pp(self):
        return "goto " + self.label.pp()

    def interp(self, env):
        rtn = "ERROR"
        return env.blk[self.label.interp()].interp(env)


class CIf:
    def __init__(self, _cmp, _l, _r):
        self.cmp = _cmp
        self.l = _l
        self.r = _r

    def pp(self):
        return "goto-if(" + self.cmp.pp() + " " + self.l.pp() + " " + self.r.pp() + ")"

    def interp(self, env):
        rtn = "ERROR"
        if(self.cmp.interp(env)):
            return env.blk[self.l.interp()].interp(env)
        else:
            return env.blk[self.r.interp()].interp(env)

#################    C2 Language  #####################


class CUnit:
    def tp(self):
        return "CUnit()"

    def typec(self, env=None):
        return "UNIT"

    def pp(self):
        return "Unit()"

    def interp(self, env):
        return self


class CAllocate:
    def __init__(self, _num, _typ):
        self.has_type = _typ
        self.num = _num
        self.args = []
        for i in range(0, _num.interp(None)):
            self.args.append(0)

    def pp(self):
        return "Allocate(" + self.num.pp() + " " + self.has_type + ")"

    def typec(self, env=None):
        temp = {}
        return temp

    def interp(self, env=None):
        return self


class CVectorSet:
    def __init__(self, _var, _ref, _exp):
        self.var = _var
        self.ref = _ref
        self.exp = _exp

    def pp(self):
        return "(VectorSet! " + self.var.pp() + " " + self.ref.pp() + " " + self.exp.pp() + ")"

    def typec(self, env=None):
        if(isinstance(self.exp, CVar)):
            env.type[self.var.pp()].update({self.ref.n: self.exp.typec(env)})
            t = env.type[self.exp.pp()]
            return t
        return self.exp.has_type

    def interp(self, env=None):
        vec = self.var.interp(env)
        if(isinstance(vec, CAllocate)):
            self.var.interp(env)
            vec.args[self.ref.interp(env)] = self.exp
        return self


class CVectorRef:
    def __init__(self, _var, _ref):
        self.var = _var
        self.ref = _ref

    def pp(self):
        return "(VectorRef! " + self.var.pp() + " " + self.ref.pp() + ")"

    def typec(self, env=None):
        if(isinstance(self.var, CVar)):
            t = env.type[self.var.pp()]
            t = t[self.ref.n]
            return t
        return self.var.has_type

    def interp(self, env=None):
        vec = self.var.interp(env)
        if(isinstance(vec, CAllocate)):
            return vec.args[self.ref.interp(env)].interp(env)
        return self


class CCollect():
    def __init__(self, _num):
        self.num = _num
        self.has_type = "NUM"

    def pp(self):
        return "Collect(" + self.num.pp() + ")"

    def tp(self):
        return "CCollect(" + self.num.tp() + ")"

    def typec(self, env=None):
        return self.has_type

    def interp(self, env=None):
        return self.num.interp(env)


class CGlobal:
    def __init__(self, _var):
        self.var = _var

    def pp(self):
        return self.var

    def typec(self, env=None):
        if(self.var in env.type):
            return env.type[self.var]
        return "ERROR"

    def interp(self, env):
        return env.var[self.var]


###################### Functions ######################
class RNGEnv:
    def __init__(self):
        self.varList = []
        self.vecList = {}
        self.varCntr = 1

    def setVarList(self, v):
        self.varList.append(v)

    def setVecList(self, v, i):
        self.vecList.update({v: i})

    def getVarList(self):
        return self.varList

    def getVecList(self):
        return self.vecList


def randomR2(n):
    random.seed(datetime.now())
    typ = random.choice(["NUM", "BOOL"])
    env = RNGEnv()
    r = _randomR2(typ, n, env)
    return r


def ranNeg(t, n, env): return RNegate(_randomR2(t, n-1, env))
def ranAdd(t, n, env): return RAdd(
    _randomR2(t, n-1, env), _randomR2(t, n-1, env))


def ranNot(t, n, env): return RNot(_randomR2(t, n-1, env))


def _randomR2(typ, n, env: RNGEnv):
    random.seed(datetime.now())
    ret = 0
    ranNum = RNum(random.randint(0, 16))
    ranBool = RBool(random.choice([True, False]))
    if(n == 0):
        if(len(env.getVarList()) > 0):
            chosenVar = [RVar(random.choice(env.getVarList()))]
        else:
            chosenVar = []
        if(len(list(env.getVecList().keys())) > 0):
            idx = 1
            if(typ == "NUM"):
                idx = 0
            chosenVec = [RVectorRef(
                RVar(random.choice(list(env.getVecList().keys()))), RNum(idx))]
        else:
            chosenVec = []
        if(typ == "NUM"):
            ret = random.choice([ranNum, RRead()])
        else:
            ret = random.choice([ranBool])
        ret = random.choice([ret] + chosenVar + chosenVec)
    else:
        if(typ == "NUM"):
            vecAvail = []
            if(env.getVecList()):
                vecAvail = ["set"]
            ret = random.choice(["add", "neg", "let", "if", "vec"] + vecAvail)
            if(ret == "add"):
                ret = ranAdd(typ, n, env)
            elif(ret == "neg"):
                ret = ranNeg(typ, n, env)
            elif(ret == "let"):
                ret = ranLet(typ, n, env)
            elif(ret == "if"):
                ret = ranIf(typ, n, env)
            elif(ret == "vec"):
                ret = ranVec(typ, n, env)
            elif(ret == "set"):
                ret = ranVecSet(typ, n, env)
        elif(typ == "BOOL"):
            vecAvail = []
            if(env.getVecList()):
                vecAvail = ["set"]
            ret = random.choice(["cmp", "let", "if", "vec"] + vecAvail)
            if(ret == "cmp"):
                ret = ranCmp(typ, n, env)
            elif(ret == "let"):
                ret = ranLet(typ, n, env)
            elif(ret == "if"):
                ret = ranIf(typ, n, env)
            elif(ret == "vec"):
                ret = ranVec(typ, n, env)
            elif(ret == "set"):
                ret = ranVecSet(typ, n, env)
    return ret


def ranLet(t, n, env: RNGEnv):
    name = "V" + str(env.varCntr)
    env.varCntr += 1
    newVar = RVar(name)
    if(t == "BOOL"):
        l = _randomR2(t, n-1, env)
        env.setVarList(name)
        r = _randomR2(t, n-1, env)
        return RLet(newVar, l, r)
    elif(t == "NUM"):
        l = _randomR2(t, n-1, env)
        env.setVarList(name)
        r = _randomR2(t, n-1, env)
        return RLet(newVar, l, r)
    print("ERROR in RAN")
    exit(1)
    return "ERROR"


def ranCmp(t, n, env: RNGEnv): return RCmp(random.choice(
    ["==", ">=", ">", "<=", "<"]), _randomR2("NUM", n-1, env), _randomR2("NUM", n-1, env))


def ranIf(t, n, env: RNGEnv):
    return RIf(ranCmp(t, n, env), _randomR2(t, n-1, env), _randomR2(t, n-1, env))


def ranVec(t, n, env: RNGEnv):
    name = "VE" + str(len(env.getVecList().keys()))
    newVar = RVar(name)
    newVec = RVector([RNum(random.randint(0, 16)),
                      RBool(random.choice([True, False]))])
    env.setVecList(name, newVec)
    return RLet(newVar, newVec, _randomR2(t, n-1, env))


def ranVecSet(t, n, env: RNGEnv):
    name = random.choice(list(env.getVecList().keys()))
    setVal = RNum(random.randint(0, 16))
    vecChoice = RVar(name)
    idx = 0
    if(t == "BOOL"):
        idx = 1
        setVal = RBool(random.choice([True, False]))
    return RLet(RVar("_"), RVectorSet(vecChoice, RNum(idx), setVal), _randomR2(t, n, env))


######## Big Mem Function ########

def bigMem(n, m):
    ans = _bigMem(n, m)
    return ans


def _bigMem(n, m):
    nums = [RNum(i) for i in range(0, m)]
    if(n == 0):
        return RVector(nums)
    else:
        nums.insert(0, RVectorRef(RVar("out"), RNum(0)))
        e = RLet(RVar("out"), _bigMem(n-1, m), RLet(RVar("i"), RVector(nums), RLet(RVar("_"), RVectorSet(RVar("i"), RNum(0),
                                                                                        RAdd(RNum(1), RVectorRef(RVar("i"), RNum(0)))), RVar("i"))))
        return e


######## Optimizer Function ########
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
        return False
    elif(isinstance(n, RLet)):
        return simple(n.l) and simple(n.r)
    elif(isinstance(n, RVector)):
        return False
    elif(isinstance(n, RVectorRef)):
        return False
    elif(isinstance(n, RVectorSet)):
        return False
    return False


class OptEnv:
    def __init__(self):
        self.env = {}
        self.renv = REnv()

    def getEnv(self):
        return self.env

    def setEnv(self, name, add):
        self.env.update({name: add})


def optimizer(n):
    env = OptEnv()
    return _optimizer(n, env)


def _optimizer(n, env: OptEnv):
    if isinstance(n, RNum):
        return n
    elif isinstance(n, RBool):
        return n
    elif isinstance(n, RRead):
        return n
    elif(isinstance(n, RCmp)):
        op = n.op
        l = n.l
        r = n.r
        return RCmp(op, _optimizer(l, env), _optimizer(r, env))
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
            #print("Add case 1")
            return RNum(l.interp() + r.interp())

        elif(isinstance(l, RNum) and isinstance(r, RAdd) and isinstance(r.left, RNum)):
            #print("Add case 2")
            return RAdd(RNum(l.interp() + r.left.interp()), _optimizer(r.right, env))

        elif(isinstance(l, RAdd) and isinstance(r, RNum) and isinstance(l.left, RNum)):
            #print("Add case 3")
            return RAdd(RNum(l.left.interp() + r.interp()), _optimizer(l.right, env))

        elif(isinstance(l, RAdd) and isinstance(l.left, RNum) and isinstance(r, RAdd) and isinstance(r.left, RNum)):
            #print("Add case 4")
            return RAdd(RNum(l.left.interp() + r.left.interp()), RAdd(_optimizer(l.right, env), _optimizer(r.right, env)))

        elif(not isinstance(l, RNum) and isinstance(r, RNum)):
            #print("Add case 5")
            return RAdd(r, _optimizer(l, env))
        else:
            #print("Add case 6")
            return RAdd(_optimizer(l, env), _optimizer(r, env))
    # elif isinstance(n, RSub):
    #     return _optimizer(RAdd(n.l, RNegate(n.r)), env)
    elif(isinstance(n, RIf)):
        var = n.var
        l = n.l
        r = n.r
        if(isinstance(var, RIf) and isinstance(l, RBool) and isinstance(r, RBool) and
           var.l.interp() == False and var.r.interp() == True):
            if(l.interp() == False and r.interp() == True):
                return _optimizer(var.var, env)
        return RIf(_optimizer(var, env), _optimizer(l, env), _optimizer(r, env))

    elif(isinstance(n, RVar)):
        if(n.name in env.getEnv()):
            if(isinstance(env.getEnv()[n.name], RVector)):
                return n
            return env.getEnv()[n.name]
        else:
            return n
    elif(isinstance(n, RLet)):
        xe = _optimizer(n.l, env)
        if(simple(xe)):
            env.setEnv(n.var.pp(), xe)
            env.renv.setEnv(n.var.pp(), xe)
            return _optimizer(n.r, env)
        else:
            env.setEnv(n.var.pp(), xe)
            env.renv.setEnv(n.var.pp(), xe)
            be = _optimizer(n.r, env)
            return RLet(n.var, xe, be)

    elif(isinstance(n, RVector)):
        vcarray = n.args
        newvcarray = []
        for e in vcarray:
            newvcarray.append(_optimizer(e, env))

        return RVector(newvcarray)
    elif(isinstance(n, RVectorRef)):
        vr = n.exp
        if(isinstance(vr, RVector)):
            actualref = _optimizer(n.ref, env)
            if(simple(actualref)):
                retref = _optimizer(vr.args[actualref.interp()], env)
                return retref
            return n
    elif(isinstance(n, RVectorSet)):
        vecr = _optimizer(n.exp, env)
        if(isinstance(vecr, RVector)):
            return n
        else:
            return RVectorSet(n.exp, n.ref, _optimizer(n.var, env))

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
    if(isinstance(e, RBool)):
        return e
    elif(isinstance(e, RRead)):
        return e
    elif(isinstance(e, RNegate)):
        return RNegate(uni(e.num, uenv))
    elif(isinstance(e, RAdd)):
        return RAdd(uni(e.left, uenv), uni(e.right, uenv))
    elif(isinstance(e, RSub)):
        return RSub(uni(e.l, uenv), uni(e.r, uenv))
    elif(isinstance(e, RCmp)):
        return RCmp(e.op, uni(e.l, uenv), uni(e.r, uenv))
    elif(isinstance(e, RAnd)):
        return RAnd(uni(e.l, uenv), uni(e.r, uenv))
    elif(isinstance(e, ROr)):
        return ROr(uni(e.l, uenv), uni(e.r, uenv))
    elif(isinstance(e, RNot)):
        return RNot(uni(e.e, uenv))
    elif(isinstance(e, RIf)):
        return RIf(uni(e.var, uenv), uni(e.l, uenv), uni(e.r, uenv))
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
    elif(isinstance(e, RVector)):
        # vecArray = e.args
        # newVecArray = []
        # for i in vecArray:
        #     newVecArray.append(uni(i, uenv))
        return e
    elif(isinstance(e, RVectorRef)):
        return RVectorRef(uni(e.exp, uenv), e.ref)
    elif(isinstance(e, RVectorSet)):
        return RVectorSet(uni(e.exp, uenv), e.ref, uni(e.var, uenv))
    print("ERROR")
    return e

########### Expose Allocation ###########


class ExpEnv():
    def __init__(self):
        self.cntr = 0
        self.letBefore = None
        self.underScoreCntr = 0
        self.varBefore = None


def exposeAllocation(r):
    env = ExpEnv()
    e = exposeAlloc(r, env)
    return e


def exposeAlloc(r, env: ExpEnv):
    if(isinstance(r, RNum)):
        return r
    elif(isinstance(r, RRead)):
        return r
    elif(isinstance(r, RBool)):
        return r
    elif(isinstance(r, RVar)):
        return r
    elif(isinstance(r, RUnit)):
        return r
    elif(isinstance(r, RNegate)):
        return RNegate(exposeAlloc(r.num, env))
    elif(isinstance(r, RAdd)):
        return RAdd(exposeAlloc(r.left, env), exposeAlloc(r.right, env))
    elif(isinstance(r, RLet)):
        if(isinstance(r.l, RVector)):
            env.letBefore = exposeAlloc(r.r, env)
            env.varBefore = r.var
            newLet = exposeAlloc(r.l, env)
            return newLet
        else:
            return RLet(exposeAlloc(r.var, env), exposeAlloc(r.l, env), exposeAlloc(r.r, env))
    elif(isinstance(r, RIf)):
        return RIf(exposeAlloc(r.var, env), exposeAlloc(r.l, env), exposeAlloc(r.r, env))
    elif(isinstance(r, RCmp)):
        return RCmp(r.op, exposeAlloc(r.l, env), exposeAlloc(r.r, env))
    elif(isinstance(r, RVectorRef)):
        return RVectorRef(exposeAlloc(r.exp, env), r.ref)
    elif(isinstance(r, RVectorSet)):
        return RVectorSet(exposeAlloc(r.exp, env), r.ref, exposeAlloc(r.var, env))
    elif(isinstance(r, RVector)):
        newVecArray = []
        oldVecArray = reversed(r.args)
        cntr = 0
        name = RVar("alloc" + str(env.cntr))
        before = RVar("alloc" + str(env.cntr))
        for e in oldVecArray:
            newVecArray.append(exposeAlloc(e, ExpEnv()))

        if(env.varBefore):
            name = env.varBefore
        if(env.letBefore):
            before = env.letBefore
        cntr = len(newVecArray)-1
        for e in newVecArray:
            before = RLet(RVar("_"), RVectorSet(name, RNum(cntr), e), before)
            cntr -= 1
            env.underScoreCntr += 1

        assignVec = RLet(name, RAllocate(RNum(len(r.args)), r.typec()), before)
        env.underScoreCntr += 1
        checkLet = RLet(RVar("_"), RIf(RCmp("<", RAdd(RGlobal("free_ptr"), RNum(8*(len(r.args)+1))), RGlobal("from_end")),  RUnit(), RCollect(RNum(len(r.args)))), assignVec)
        env.cntr += 1
        env.varBefore = None
        env.letBefore = None
        return checkLet

########### Resolve Complex ###########


class RCOEnv:
    def __init__(self):
        self.varCntr = 0
        self.lifts = []
        self.env = {}

    def getEnv(self):
        return self.env

    def setEnv(self, name, add):
        self.env[name] = add

    def getLift(self):
        return self.lifts

    def setLift(self, add):
        self.lifts.insert(0, add)

    def incCntr(self):
        self.varCntr += 1
        return self.varCntr


def RCO(e):
    env = RCOEnv()
    isTail = True
    rtn = _rco(isTail, env, e)
    return letStar(rtn, env)


def _rcoLift(env, e):
    indx = env.incCntr()
    nv = "R" + str(indx)
    env.setLift((RVar(nv), e))
    return RVar(nv)


def _rco(isTail, env: RCOEnv, e):
    if(isinstance(e, RNum)):
        return _rcoLift(env, e)
    if(isinstance(e, RBool)):
        return _rcoLift(env, e)
    elif(isinstance(e, RRead)):
        return _rcoLift(env, e)

    elif(isinstance(e, RNegate)):
        ep = _rco(False, env, e.num)
        return _rcoLift(env, RNegate(ep))
    elif(isinstance(e, RNot)):
        ep = _rco(False, env, e.e)
        return _rcoLift(env, RNot(ep))

    elif(isinstance(e, RAdd)):
        lp = _rco(False, env, e.left)
        rp = _rco(False, env, e.right)
        return _rcoLift(env, RAdd(lp, rp))
    elif(isinstance(e, RCmp)):
        lp = _rco(False, env, e.l)
        rp = _rco(False, env, e.r)
        return _rcoLift(env, RCmp(e.op, lp, rp))
    elif(isinstance(e, RIf)):
        cmpp = rco_c(False, e.var, env)
        t = _rco(isTail, env, e.l)
        f = _rco(isTail, env, e.r)
        ifp = RIf(cmpp, t, f)
        if(isTail):
            return ifp
        else:
            return _rcoLift(env, ifp)
    elif(isinstance(e, RVar)):
        if(e.name in env.getEnv()):
            return env.getEnv()[e.name]
        else:
            print("RCO UNBOUND")
            return "FAILURE"
    elif(isinstance(e, RLet)):
        if(isinstance(e.var, RGlobal)):
            env.setLift((e.var, e.l))
            return _rco(isTail, env, e.r)
        lp = _rco(False, env, e.l)
        env.setEnv(e.var.name, lp)
        return _rco(isTail, env, e.r)

    elif(isinstance(e, RVector)):
        print("RCO UNBOUND Shouldn't see Vectors")
        return "ERROR"
    elif(isinstance(e, RVectorSet)):
        exp = _rco(False, env, e.exp)
        # ref = _rco(False, env, e.ref)
        var = _rco(False, env, e.var)
        return _rcoLift(env, RVectorSet(exp, e.ref, var))
    elif(isinstance(e, RVectorRef)):
        exp = _rco(False, env, e.exp)
        # ref = _rco(False, env, e.ref)
        return _rcoLift(env, RVectorRef(exp, e.ref))
    elif(isinstance(e, RAllocate)):
        return _rcoLift(env, e)
    # elif(isinstance(e, RCollect)):
    #     return _rcoLift(env, e)
    else:
        return e


def letStar(fa, env: RCOEnv):
    if not env.getLift():
        return fa
    else:
        var, eq = env.getLift().pop()
        return RLet(var, eq, letStar(fa, env))


def rco_c(isTail, e, env: RCOEnv):
    if(isinstance(e, RCmp)):
        l = _rco(isTail, env, e.l)
        r = _rco(isTail, env, e.r)
        return RCmp(e.op, l, r)
    elif(isinstance(e, RLet)):
        lp = _rco(isTail, env, e.l)
        env.setEnv({e.var.name: lp})
        return rco_c(isTail, env, e.r)
    else:
        ep = _rco(isTail, env, e)
        return RCmp("==", RBool(True), ep)

######## Explicate Control Pass ########


class EconEnv:
    def __init__(self):
        self.p = {}
        self.cntr = 0
        self.curLab = "main"

    def addEnv(self, lab, s):
        if(lab in self.p):
            self.p[lab].append(s)
        else:
            self.p.update({lab: [s]})

    def getEnv(self):
        return self.p


def econ(r):
    env = EconEnv()
    rtn = econHelper(r, env)
    actualP = {}
    for l, b in env.p.items():
        actualP.update({CLabel(l): CBlock(None, b)})
    p = CProgram(None, actualP)
    return p


def econArgs(r):
    if(isinstance(r, RNum)):
        return CNum(r.num)
    elif(isinstance(r, RVar)):
        return CVar(r.name)
    elif(isinstance(r, RBool)):
        return CBool(r.b)
    elif(isinstance(r, RUnit)):
        return CUnit()
    elif(isinstance(r, RCollect)):
        return CCollect(econArgs(r.num))
    elif(isinstance(r, RGlobal)):
        return CGlobal(r.name)
    else:
        return "ERROR"


def econExp(r):
    if(isinstance(r, RRead)):
        return CRead()
    elif(isinstance(r, RNegate)):
        return CNeg(econArgs(r.num))
    elif(isinstance(r, RNot)):
        return CNot(econArgs(r.e))
    elif(isinstance(r, RAdd)):
        return CAdd(econArgs(r.left), econArgs(r.right))
    elif(isinstance(r, RCmp)):
        return getOp(r)
    elif(isinstance(r, RVectorRef)):
        return CVectorRef(econArgs(r.exp), econArgs(r.ref))
    elif(isinstance(r, RVectorSet)):
        return CVectorSet(econArgs(r.exp), econArgs(r.ref), econArgs(r.var))
    elif(isinstance(r, RAllocate)):
        return CAllocate(econArgs(r.num), r.has_type)
    else:
        return econArgs(r)


def getForm(a):
    if(isinstance(a, RNum) or isinstance(a, RBool) or isinstance(a, RRead) or isinstance(a, RVar) or isinstance(a, RGlobal)):
        return True
    return False


def econHelper(r, env: EconEnv):
    #print(env.curLab + " "+ r.pp())
    if(isinstance(r, RLet)):
        if(isinstance(r.l, RIf)):
            if(getForm(r.l.l) and getForm(r.l.r)):
                env.addEnv(env.curLab, CSetCC(getOp(r.l.var), econArgs(
                    r.var), econArgs(r.l.l), econArgs(r.l.r)))
                return econHelper(r.r, env)
            tp = r.l.l
            fp = r.l.r
            blab = "label" + str(env.cntr+3)
            tlab = econLabel(tp, env)
            temp = env.getEnv()[tlab.label][-1]
            if(isinstance(temp, CRet)):
                setvar = temp.var
                env.getEnv()[tlab.label][-1] = CSet(CVar(r.var.pp()), setvar)
                env.addEnv(tlab.label, CGoto(CLabel(blab)))
            flab = econLabel(fp, env)
            temp = env.getEnv()[flab.label][-1]
            if(isinstance(temp, CRet)):
                setvar = temp.var
                env.getEnv()[flab.label][-1] = CSet(CVar(r.var.pp()), setvar)
                env.addEnv(flab.label, CGoto(CLabel(blab)))
            env.addEnv(env.curLab, CIf(getOp(r.l.var), tlab, flab))
            env.cntr = env.cntr+1
            env.curLab = blab
            return econHelper(r.r, env)
        else:
            a = CSet(econArgs(r.var), econExp(r.l))
            env.addEnv(env.curLab, a)
            return econHelper(r.r, env)

    elif(isinstance(r, RIf)):
        if(isinstance(r.var, RCmp)):
            tp = r.l
            fp = r.r
            tlab = econLabel(tp, env)
            flab = econLabel(fp, env)
            env.addEnv(env.curLab, CIf(getOp(r.var), tlab, flab))
            return
    elif(isinstance(r, RVar)):
        return env.addEnv(env.curLab, CRet(econArgs(r)))

    else:
        return env.addEnv(env.curLab, CRet(econArgs(r)))


def getOp(cmp: RCmp):
    if(isinstance(cmp, RCmp)):
        if(cmp.op == "=="):
            return CCmp("==", econExp(cmp.l), econExp(cmp.r))
        elif(cmp.op == ">"):
            return CCmp(">", econExp(cmp.l), econExp(cmp.r))
        elif(cmp.op == ">="):
            return CCmp(">=", econExp(cmp.l), econExp(cmp.r))
        elif(cmp.op == "<"):
            return CCmp("<", econExp(cmp.l), econExp(cmp.r))
        elif(cmp.op == "<="):
            return CCmp("<=", econExp(cmp.l), econExp(cmp.r))
        else:
            return "ERROR"
    else:
        return econExp(cmp)


def econLabel(e, env: EconEnv):
    env.cntr = env.cntr+1
    lTitle = "label" + str(env.cntr)
    temp = env.curLab
    env.curLab = lTitle
    t = econHelper(e, env)
    #print("WORKING WITH IF LABVELS" + newS.pp())
    env.curLab = temp
    return CLabel(lTitle)


######## Uncover Local Pass ########
def uncoverLocal(e: CProgram):
    varList = {}
    uncEnv = CEnv()
    for l, b in e.p.items():
        for s in b.p:
            if(isinstance(s, CSet)):
                a = s.typec(uncEnv)
                if(isinstance(a,dict)):
                    if(not s.var in varList):
                        if(isinstance(s.var, CVar)):
                            varList.update({s.var.pp(): {"VECTOR":a}})
                else:
                    if(not s.var in varList):
                        if(isinstance(s.var, CVar)):
                            varList.update({s.var.pp(): a})

    e.info = varList
    return e


######## Select Instr Pass ########

class SelEnv:
    def __init__(self):
        self.vars = []
        self.globals = []
        self.typecntr =0

    def setEnv(self, add):
        self.vars(add)

    def getEnvInd(self, name):
        return self.vars[name]

    def getEnv(self):
        return self.vars




def select(cp: CProgram):
    env = SelEnv()
    blk = {}
    for lab, lin in cp.p.items():
        tempBlk = []
        tempLabel = XLabel(lab.interp())
        if(isinstance(lin, CBlock)):
            for l in lin.p:
                rtn = _selectT(l, tempBlk, env, cp.info)
                if(isinstance(rtn, list)):
                    tempBlk = tempBlk + rtn
                else:
                    tempBlk.append(rtn)
        blk.update({tempLabel: XBlock([], tempBlk)})
    blk.update({XLabel("end"): XBlock([], [XIRet()])})
    return XProgram(env.globals, cp.info, blk)

def selectGetType(var: XVar, info, env: SelEnv):
    tempType = "type" + str(env.typecntr)
    tempTypeArr = info[var.name]["VECTOR"]
    tempTypeStr =tempType + ":\n.quad 3\n.quad " + str(len(tempTypeArr.values())) + "\n"
    for i,t in tempTypeArr.items():
        if(t == "NUM"):
            tempTypeStr += ".quad 1\n"
        elif(t == "BOOL"):
            tempTypeStr += ".quad 2\n"
    env.globals.append(tempTypeStr)
    env.typecntr+=1
    return XType(tempType)

def _selectT(cp, arr, env, info):
   
    if isinstance(cp, CRet):
        return [XIMov(_selectA(cp.var, env), XRegister("rax")), XIJmp(XLabel("end"))]
    elif(isinstance(cp, CSet)):
        src = cp.exp
        dst = cp.var
        if(isinstance(src, CAllocate)):
            vecDst = _selectA(dst, env)
            tempType = selectGetType(vecDst, info, env)
            return [XIMov(XGlobal("free_ptr"), vecDst),
                    XIAdd(XCon(wordsize*(1+src.num.n)), XGlobal("free_ptr")),
                    XIMov(vecDst, tempReg2),
                    XILeaq(tempType, tempReg),
                    XIMov(tempReg, XMem(tempReg2,0))
            ]
        elif(isinstance(src, CVectorRef)):
            vecName = _selectA(src.var, env)
            print(vecName.emit())
            vecDst = _selectA(dst, env)
            return [XIMov(vecName, tempReg), 
                    XIMov(XMem(tempReg2, wordsize*(src.ref.n+1)), vecDst)
                    ]
        elif(isinstance(src, CVectorSet)):
            vecName = _selectA(src.var, env)
            vecArg = _selectA(src.exp, env)
            vecDst = _selectA(dst, env)
            return [XIMov(vecName, tempReg2),
                    XIMov(vecArg, tempReg),
                    XIMov(tempReg, XMem(tempReg2, 8*(src.ref.n+1))), 
                ]
        elif(isinstance(src, CCollect)):
            vecDst = _selectA(dst, env)
            colNum = src.num.n*8
            return [
                XIMov(XCon(colNum), XRegister("rdi")), XIMov(root_stack_reg, XRegister("rsi")), XICall(XLabel("collect")), XIMov(XCon(1), vecDst)
            ]
        return _selectE(src, dst, env)
    elif(isinstance(cp, CSetCC)):
        cmp = cp.cmp
        actualCmp = None
        op = None
        if(isinstance(cmp, CCmp)):
            actualCmp = XICmp(_selectA(cmp.l, env), _selectA(cmp.r, env))
            op = _selectC(cmp)
            return [actualCmp, XIMov(_selectA(cp.f, env), _selectA(cp.var, env)), XICMov(op, _selectA(cp.t, env), _selectA(cp.var, env))]
        return []
    elif(isinstance(cp, CIf)):
        cmp = cp.cmp
        actualCmp = None
        op = None
        if(isinstance(cmp, CCmp)):
            actualCmp = XICmp(_selectA(cmp.l, env), _selectA(cmp.r, env))
            op = _selectC(cmp)
            return [actualCmp, XIJmpIf(op, XLabel(cp.l.pp())), XIJmp(XLabel(cp.r.pp()))]
        return []
    elif(isinstance(cp, CGoto)):
        return XIJmp(XLabel(cp.label.pp()))


def _selectE(cp, dst, env):
    if(isinstance(cp, CRead)):
        return [XICall(XLabel("read_int")), XIMov(XRegister("rax"), _selectA(dst, env))]
    elif(isinstance(cp, CNeg)):
        return [XIMov(_selectA(cp.n, env), _selectA(dst, env)), XINeg(_selectA(dst, env))]
    elif(isinstance(cp, CAdd)):
        return [XIMov(_selectA(cp.l, env), _selectA(dst, env)), XIAdd(_selectA(cp.r, env), _selectA(dst, env))]
    elif(isinstance(cp, CNot)):
        return [XIMov(_selectA(cp.e, env), _selectA(dst, env)), XIXor(XCon(1), _selectA(dst, env))]
    elif(isinstance(cp, CCmp)):
        return [XICmp(_selectA(cp.l, env), _selectA(cp.r, env)), XISet(_selectC(cp), XByteRegister("al")),
                XIMovzb(XByteRegister("al"), _selectA(dst, env))]
    else:
        return XIMov(_selectA(cp, env), _selectA(dst, env))


def addGlobal(g, env):
    inGlobal = False
    for i in env.globals:
        if(isinstance(i, XGlobal)):
            if(i.var == g.var):
                inGlobal = True
    if(not inGlobal):
        env.globals.append(g)
    return


def _selectA(cp, env):
    if(isinstance(cp, CNum)):
        return XCon(cp.n)
    elif(isinstance(cp, CVar)):
        return XVar(cp.pp())
    elif(isinstance(cp, CBool)):
        return XCon(int(cp.b))
    elif(isinstance(cp, CUnit)):
        return XCon(1)
    elif(isinstance(cp, CGlobal)):
        #addGlobal(XGlobal(cp.pp()), env)
        return XGlobal(cp.var)


def _selectC(cp: CCmp):
    if(cp.op == ">"):
        return XG()
    elif(cp.op == ">="):
        return XGEq()
    elif(cp.op == "<"):
        return XL()
    elif(cp.op == "<="):
        return XLEq()
    elif(cp.op == "=="):
        return XEq()


######## Uncover Live ########
class UNCEnv:
    def __init__(self):
        self.live_sets = {}
        self.current_set = set([])
    def setEnv(self, inst, before):
        self.live_sets.update({inst: before})

def uncover_live(xp: XProgram):
    m = {}
    l =UNCEnv()
    labList =[]
    for lab, blk in xp.p.items():
        if(isinstance(lab,XLabel) and isinstance(blk, XBlock)):
            m[lab.string] = []
            labList.append(lab.string)
            for i in reversed(blk.blk):
                m[lab.string].append(i)

    curLab = "main"           
    blk =m[curLab]
    live_e(blk, l, m, curLab)
    print("LIVE" + str(l))
    return l.live_sets


def live_e(blk:list, live_sets:dict, m:dict, lab:str):
    before = set([])
    if(lab == "end"):
        return set([])
    for i in blk:
        before = live_i(before, i, live_sets, m, lab)
        print(before)
    return before


def live_i(before:set, i, live_sets:UNCEnv, m:dict, lab:str):

    if(isinstance(i, XIJmp)):
        #live_sets.update({i: before})
        live_e(m[i.src.string], live_sets, m, i.src)
        return live_sets.current_set
        # m[i.src.emit()].update({i.src.emit():before})
    elif(isinstance(i, XIJmpIf)):
        #live_sets.update({i: before})
        live_e(m[i.label.string], live_sets, m, i.label)
        return live_sets.current_set
        # m[lab].update({i: before})
        # m[i.label.string] = m[lab]
        # m[i.label.emit()].update({i.label.emit():before})
    elif(isinstance(i, XIRet)):
        return
    else:
        live_sets.setEnv(i, before)
        #print("Live before: " + str(n) +" = " + str(before), end=' ')
        # print(w)
        # print(r)
        live_sets.current_set = live_sets.current_set - _uncoverW(i)
        live_sets.current_set = before.union(_uncoverR(i))
        
    return live_sets.current_set


def _uncoverW(i):
    if(isinstance(i, XINeg)):
        return _uncoverM(i.src, True)
    elif(isinstance(i, XIAdd)):
        return _uncoverM(i.dst, True)
    elif(isinstance(i, XISub)):
        return _uncoverM(i.dst, True)
    elif(isinstance(i, XIMov)):
        return _uncoverM(i.dst, True)
    elif(isinstance(i, XILeaq)):
        return _uncoverM(i.dst, True)
    elif(isinstance(i, XICMov)):
        return _uncoverM(i.dst, True)
    elif(isinstance(i, XIPush)):
        return set([])
    elif(isinstance(i, XIPop)):
        return _uncoverM(i.src, True)
    elif(isinstance(i, XIMovzb)):
        return _uncoverM(i.r, True)
    elif(isinstance(i, XILeaq)):
        return _uncoverM(i.dst, True)
    elif(isinstance(i, XIXor)):
        return _uncoverM(i.r, True)
    elif(isinstance(i, XICmp)):
        return set([])
    elif(isinstance(i, XISet)):
        return _uncoverM(i.arg, True)
    elif(isinstance(i, XIJmp)):
        return set([])
    elif(isinstance(i, XIJmpIf)):
        return set([])
    elif(isinstance(i,XICall)):
        return set([i.emit() for i in callerSavedRegs])
    elif(isinstance(i,XICMov)):
        return _uncoverM(i.dst, True)
    return set([])


def _uncoverR(i):
    if(isinstance(i, XINeg)):
        return _uncoverM(i.src, False)
    elif(isinstance(i, XIAdd)):
        return _uncoverM(i.dst, False).union(_uncoverM(i.src, False))
    elif(isinstance(i, XISub)):
        return _uncoverM(i.dst, False).union(_uncoverM(i.src, False))
    elif(isinstance(i, XIMov)):
        return _uncoverM(i.src, False)
    elif(isinstance(i, XILeaq)):
        return _uncoverM(i.src, False)
    elif(isinstance(i, XICMov)):
        return _uncoverM(i.src, False)
    elif(isinstance(i, XIPush)):
        return _uncoverM(i.src, False)
    elif(isinstance(i, XIPop)):
        return set([])
    elif(isinstance(i, XIXor)):
        return _uncoverM(i.r, False).union(_uncoverM(i.l, False))
    elif(isinstance(i, XIMovzb)):
        return _uncoverM(i.l, False)
    elif(isinstance(i, XILeaq)):
        return _uncoverM(i.dst, False)
    elif(isinstance(i, XICmp)):
        return _uncoverM(i.r, False).union(_uncoverM(i.l, False))
    elif(isinstance(i, XISet)):
        return _uncoverM(i.arg, False)
    elif(isinstance(i, XIJmp)):
        return set([])
    elif(isinstance(i, XIJmpIf)):
        return set([])
    elif(isinstance(i,XICall)):
        return set([i.emit() for i in argumentRegs])
    elif(isinstance(i,XICMov)):
        return _uncoverM(i.src, True)
    return set([])


def _uncoverM(a, isWrite) ->set:
    if(isinstance(a, XRegister)):
        return set([a.emit()])
    elif(isinstance(a, XVar)):
        return set([a.emit()])
    elif(isinstance(a, XByteRegister)):
        return set([a.emit()])
    elif(isinstance(a, XMem)):
        reg = a.reg
        if(isWrite):
            return set([])
        return set([reg.emit()])
    else:
        return set([])


def printUncover(liv: dict):
    for i, a in liv.items():
        print(i.emit() + " " + str(a))
        # for i, s in values.items():
        #     print(i.emit() + " " + str(s))

######## Build Interferences ########


def buildInt(xp: XProgram, live: dict):
    g = Graph()
    m = Graph()
    for i, s in live.items():
        if(isinstance(i, XIMov)):
            if(s):
                movlike(s, i.dst, i.src, m, g)
        elif(isinstance(i, XILeaq)):
            if(s):
                movlike(s, i.dst, i.src, m, g)
        elif(isinstance(i, XIAdd)):
            if(s):
                addlike(s, i.dst, g)

        elif(isinstance(i, XINeg)):
            if(s):
                addlike(s, i.src, g)

        elif(isinstance(i, XICall)):
            pass
            if(s):
                for e in s:
                    for u in callerSavedRegs:
                        if(not u == e):
                            g.add_edge(u.emit(), str(e))
                    #When e is a vector get put on root stack
                    # for u in calleeSavedRegs:
                    #     if(not u == e):
                    #         g.add_edge(u.emit(), str(e))
        elif(isinstance(i, XIPop)):
            if(s):
                addlike(s, i.src, g)

        elif(isinstance(i, XIRet)):
            pass

        elif(isinstance(i, XIJmp)):
            pass

        elif(isinstance(i, XIXor)):
            if(s):
                addlike(s, i.r, g)

        elif(isinstance(i, XICmp)):
            pass
        elif(isinstance(i, XISet)):
            if(s):
                addlike(s, i.arg, g)

        elif(isinstance(i, XICMov)):
            if(s):
                movlike(s, i.dst, i.src, m, g)

        elif(isinstance(i, XIMovzb)):
            if(s):
                movlike(s, i.r, i.l, m, g)

        elif(isinstance(i, XIJmpIf)):
            pass
    return (g,m)


def movlike(s, d, sr, m: Graph, g: Graph):
    d = d.emit()
    sr = sr.emit()
    for e in s:
        if(not (d == e or e == sr)):
            g.add_edge(d, str(e))
        m.add_edge(sr, d)


def addlike(s, i, g: Graph):
    d = i.emit()
    for e in s:
        if(not d == e):
            g.add_edge(d, str(e))


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


def color(xp: XProgram, bldG: Graph, bldM:Graph, mov) -> XProgram:
    g = bldG
    m =[]
    if(mov):
        m = bldM
    if(g.vert_dict):
        w = list(g.vert_dict.copy())
        colorList = dict()
        available = dict()
        cntr =0
        regCntr = -2
        for x in g.vert_dict:
            if(x[0] == '%'):
                colorList.update({x: regCntr})
                available.update({cntr: True})
                regCntr-=1
            else:
                colorList.update({x: -1})
                available.update({cntr: False})
            cntr+=1
        
        colorList[w[0]] = 0
        
        while w:
            u = w[0]
            color = 0
            mvadj = None
            adj = saturation(g.vert_dict[u])
            if(m and u in m.vert_dict):
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
                    color =e
                    break
            
            colorList[u] = color

            for e in adj:
                if(e in colorList and colorList[e] != -1):
                    available[colorList[e]] = False
            
            w.remove(u)
        if(colorList):
            ss = 0
            actualRegsList ={}
            leftover =[]
            print(colorList)
            regsWithColor = dict(enumerate(usableRegs))
            print(regsWithColor)
            for name, i in colorList.items():
                if(name[0] == "!" and i in regsWithColor):
                    temp = regsWithColor[i]
                    actualRegsList.update({name:temp})
            for var, t in xp.info.items():
                leftover.append("!" + var)

            for v in leftover:
                if(not v in actualRegsList.keys()):
                    actualRegsList.update({v:XMem(XRegister("rsp"), ss)})
                    ss+=8
            print("REGS with COLOR: " )
            for a, b  in actualRegsList.items():
                print(a +" "+ b.emit())
            return (actualRegsList, ss)
    return ({}, 0)

################ Allocate Registers ################

def allocate_registers(xp: XProgram, type: str) -> XProgram:
    mStackAllocSize = 0
    live = uncover_live(xp)
    printUncover(live)
    bldG, bldM = buildInt(xp, live)
    # printGrph(bldG)
    # printGrph(bldM)
    colorList, mStackAllocSize = color(xp, bldG, bldM, 0)
    print(colorList)
    print(mStackAllocSize)

    newXp = assign_register(xp, colorList, mStackAllocSize)
    newXp = mainpass(newXp, mStackAllocSize, type)
    newXp = patch(newXp)
    return newXp

################ Assign Registers ################


def assign_register(xp: XProgram, regsList, stackSize) -> XProgram:
    originalMain = []
    body = []
    progm = {}
    for lab, blk in xp.p.items():
        body = []
        regs = regsList
        if(lab.emit() == "main"):
            originalMain = blk.blk
            for instr in originalMain:
                body.append(_assign(instr, regs))
            # body = body[:-1]
            # body.append(XIJmp(XLabel("end")))
            progm.update({XLabel("body"): XBlock([], body)})
        else:
            temp = blk.blk
            for instr in temp:
                body.append(_assign(instr, regs))
            progm.update({lab: XBlock([], body)})

    return XProgram(xp.globals, xp.info, progm)


def _assign(xp, regs):
    if(isinstance(xp, XIAdd)):
        return XIAdd(_assignA(xp.src,  regs), _assignA(xp.dst,  regs))
    elif(isinstance(xp, XISub)):
        return XISub(_assignA(xp.src, regs), _assignA(xp.dst,  regs))
    elif(isinstance(xp, XIMov)):
        return XIMov(_assignA(xp.src,  regs), _assignA(xp.dst, regs))
    elif(isinstance(xp, XILeaq)):
        return XILeaq(_assignA(xp.src,  regs), _assignA(xp.dst, regs))
    elif(isinstance(xp, XINeg)):
        return XINeg(_assignA(xp.src,  regs))
    elif(isinstance(xp, XIPush)):
        return XIPush(_assignA(xp.src,  regs))
    elif(isinstance(xp, XIPop)):
        return XIPop(_assignA(xp.src, regs))
    elif(isinstance(xp, XIMovzb)):
        return XIMovzb(_assignA(xp.l,  regs), _assignA(xp.r, regs))
    elif(isinstance(xp, XICMov)):
        return XICMov(xp.cc, _assignA(xp.src,  regs), _assignA(xp.dst, regs))
    elif(isinstance(xp, XIXor)):
        return XIXor(_assignA(xp.l,  regs), _assignA(xp.r,  regs))
    elif(isinstance(xp, XICmp)):
        return XICmp(_assignA(xp.l,  regs), _assignA(xp.r,  regs))
    elif(isinstance(xp, XISet)):
        return XISet(xp.cc, _assignA(xp.arg,  regs))
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

def mainpass(xp: XProgram, alloc: int, type: str):
    mainBdy = []
    endBlk = []
    for lab in xp.p.keys():
        if(lab.emit() == "end"):
            xp.p.pop(lab)
            break
    mainBdy = [XIPush(XRegister("rbx")), XIPush(XRegister("rbp")), XIPush(root_stack_reg), XIMov(
            XRegister("rsp"), XRegister("rbp"))]
    endBlk =  [
            XIMov(XType(type), XRegister("rdi")),
            XIMov(XRegister("rax"), XRegister("rsi")),
            XICall(XLabel("print_value"))
        ] 
    if(alloc > 0):
        mainBdy = mainBdy + \
            [XISub(XCon(alloc), XRegister("rsp"))] 
        endBlk = endBlk +[XIAdd(XCon(alloc), XRegister("rsp")), XIPop(root_stack_reg), XIPop(XRegister("rbp")), XIPop(XRegister("rbx"))]
        # for r in calleeSavedRegs:
        #     mainBdy.append(XIPush(r))
        #     endBlk.append(XIPop(r))
        
    #else:
        # for r in calleeSavedRegs:
        #     mainBdy.append(XIPush(r))
        #     endBlk.append(XIPop(r))
        # mainBdy = mainBdy + \
        #     [XIJmp(XLabel("body"))]

    mainBdy = mainBdy + [XICall(XLabel("init_mem")), XIMov(XGlobal("rootstack_start"), XRegister("r12")), XIJmp(XLabel("body"))]
    main = {XLabel("main"): XBlock([], mainBdy)}
    end = {XLabel("end"): XBlock([], endBlk +[XIRet()])}
    xp.p.update(main)
    xp.p.update(end)

    return XProgram(xp.globals, xp.info, xp.p)


def getPrintType(ty:str):
    if(ty == "UNIT"):
        return [
            XIMov(XType(ty), XRegister("rdi")),
            XIMov(XRegister("rax"), XRegister("rsi")),
            XICall("print_value")
        ]

######## Patch Instr ########

###Add function to check for Mem Ref

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
        return XProgram(xp.globals, xp.info, newP)


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
        elif(isinstance(i.src, XMem) and isinstance(i.dst, XGlobal)):
            return [XIMov(i.src, XRegister("rax")), XIMov(XRegister("rax"), i.dst)]
        elif(isinstance(i.src, XGlobal) and isinstance(i.dst, XMem)):
            return [XIMov(i.src, XRegister("rax")), XIMov(XRegister("rax"), i.dst)]
    elif(isinstance(i, XILeaq)):
        if(i.dst.emit() == i.src.emit()):
            return []
        if(isinstance(i.src, XMem) and isinstance(i.dst, XMem)):
            return [XILeaq(i.src, XRegister("rax")), XILeaq(XRegister("rax"), i.dst)]
    elif(isinstance(i, XIMovzb)):
        if(i.r.emit() == i.l.emit()):
            return []
        if(isinstance(i.r, XMem)):
            return [XIMovzb(XByteRegister("al"),XRegister("rax")), XIMov(XRegister("rax"),i.r)]
        elif(isinstance(i.l, XCon)):
            return [XIMovzb(i.l, XRegister("al")), XIMovzb(XRegister("al"), i.r)]
        elif(isinstance(i.r, XCon)):
            return [XIMovzb(i.r, XRegister("al")), XIMovzb(XRegister("al"), i.l)]
    elif(isinstance(i, XICmp)):
        if(isinstance(i.l, XMem) and isinstance(i.r, XMem)):
            return [XIMov(i.l, XRegister("rax")), XICmp(XRegister("rax"), i.r)]
        elif(isinstance(i.l, XMem) and isinstance(i.r, XGlobal)):
            return [XIMov(i.l, XRegister("rax")), XICmp(XRegister("rax"), i.r)]
        elif(isinstance(i.l, XGlobal) and isinstance(i.r, XMem)):
            return [XIMov(i.l, XRegister("rax")), XICmp(XRegister("rax"), i.r)]
        elif(isinstance(i.l, XCon)):
            return [XIMov(i.l, XRegister("rax")), XICmp(XRegister("rax"), i.r)]
        elif(isinstance(i.r, XCon)):
            return [XIMov(i.r, XRegister("rax")), XICmp(XRegister("rax"), i.l)]
    return [i]

class EmitEnv():
    def __init__(self):
        self.types = []
        self.globals = [XType("T_Unit"), XType("T_S64"), XType("T_Bool"), XType("T_Vector")]
        self.typecntr = 0

def emitXP(xp: XProgram):
    finalP = ""
    emitenv = EmitEnv()
    sectionInfo = ".section\t.data\n" + emitG(xp, emitenv)
    for t in xp.globals:
        sectionInfo += t
    sectionText = ".section\t.text\n.global main \n\n"
    blkDict = xp.p
    pStr = ""
    for lab, blk in blkDict.items():
        pStr += emitL(lab, emitenv) + "\n"
        pStr += emitB(blk, emitenv)
    print(xp.info)
    finalP += sectionInfo + sectionText + pStr + "\n\n"
    return finalP

def emitG(xp: XProgram, emitenv: EmitEnv):
    temp =""
    for g in emitenv.globals:
        if(isinstance(g, XGlobal) and g.var == "free_ptr"):
            temp +=  g.var + ":\t.quad\t0\n"
        elif(isinstance(g, XGlobal) and g.var == "from_end"):
            temp += g.var + ":\t.quad\t"+ str(1024*1024*1024) +"\n"
        elif(isinstance(g, XType) and g.t == "T_Unit"):
            temp += ".global " + g.t + "\n" + g.t +":\t.quad\t" + str(0) +"\n"
        elif(isinstance(g, XType) and g.t == "T_S64"):
            temp += ".global " + g.t + "\n" + g.t +":\t.quad\t" + str(1) +"\n"
        elif(isinstance(g, XType) and g.t == "T_Bool"):
            temp += ".global " + g.t + "\n" + g.t +":\t.quad\t" + str(2) +"\n"
        elif(isinstance(g, XType) and g.t == "T_Vector"):
            temp += ".global " + g.t + "\n" + g.t +":\t.quad\t" + str(3) +"\n"
    return temp

def emitL(lab:XLabel, env:EmitEnv):
    return lab.string + ":"

def emitB(xb: XBlock, env:EmitEnv):
    blkArray = xb.blk
    blkStr = ""
    for instr in blkArray:
        blkStr+= emitInstr(instr, env) + "\n"
    return blkStr

def emitInstr(i, env:EmitEnv):
    if(isinstance(i, XIAdd)):
        return "addq" + " " + emitA(i.src, env) + ", " + emitA(i.dst, env)
    elif(isinstance(i, XISub)):
        return "subq" + " " + emitA(i.src, env)  + ", " + emitA(i.dst, env)
    elif(isinstance(i, XIMov)):
        return "movq" + " " + emitA(i.src, env) + ", " + emitA(i.dst, env)
    elif(isinstance(i, XICMov)):
        return "cmov" + i.cc.c+ " " + emitA(i.src, env)  + ", " + emitA(i.dst, env)
    elif(isinstance(i, XINeg)):
        return "negq" + " " + emitA(i.src, env) 
    elif(isinstance(i, XICall)):
        return "callq" + " " + i.src.string
    elif(isinstance(i, XIJmp)):
        return "jmp" + " " + i.src.string
    elif(isinstance(i, XIPush)):
        return "pushq" + " " + emitA(i.src, env) 
    elif(isinstance(i, XIPop)):
        return "popq" + " " + emitA(i.src, env) 
    elif(isinstance(i, XIXor)):
        return "xorq" + " " + emitA(i.l, env)  + ", " + emitA(i.r, env)
    elif(isinstance(i, XICmp)):
        return "cmpq" + " " + emitA(i.r, env)  + ", " + emitA(i.l, env)
    elif(isinstance(i, XISet)):
        return "set" + i.cc.c  + " " + emitA(i.arg, env)
    elif(isinstance(i, XIMovzb)):
        return "movzbq" + " " + emitA(i.l, env) + ", " + emitA(i.r, env)
    elif(isinstance(i, XIJmpIf)):
        return "j" + i.cc.c + " " + i.label.string
    elif(isinstance(i, XILeaq)):
        return "leaq " + emitA(i.src, env) + ", " + emitA(i.dst, env)
    elif(isinstance(i, XIRet)):
        return "retq"

def emitA(arg, env:EmitEnv):
    if(isinstance(arg, XCon)):
        return "$" + str(arg.value)
    elif(isinstance(arg, XRegister)):
        return "%" + str(arg.register)
    elif(isinstance(arg, XByteRegister)):
        return "%" + str(arg.r)
    elif(isinstance(arg, XMem)):
        rp = emitA(arg.reg, env)
        return str(arg.num) + "("+ rp + ")"
    elif(isinstance(arg, XVar)):
        return "!" + arg.name
    elif(isinstance(arg, XGlobal)):
        return arg.var + "(" + emitA(XRegister("rip"), env) + ")"
    elif(isinstance(arg, XType)):
        if(arg.t == "Unit"):
            return "T_Unit" + "(" + emitA(XRegister("rip"), env) + ")" 
        elif(arg.t == "NUM"):
            return "T_S64" + "(" + emitA(XRegister("rip"), env) + ")" 
        elif(arg.t == "BOOL"):
            return "T_Bool" + "(" + emitA(XRegister("rip"), env) + ")" 
        elif(arg.t == "VECTOR"):
            return "T_Vector" + "(" + emitA(XRegister("rip"), env) + ")" 
        return arg.t + "(" + emitA(XRegister("rip"), env) + ")" 
