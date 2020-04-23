from string import ascii_lowercase, ascii_uppercase, digits
import re
error = ('err', 'error')
unit = ('unit', 'unit')


def isName(value):
    return re.match(r'_?[A-Za-z][A-Za-z0-9_]*', value)


def fetch(v, envs):
    if v[0] in ['str', 'bool', 'err', 'int', 'unit']:
        return v
    for env in reversed(envs):
        for (n, val) in reversed(env):
            if n == v[1]:
                return val
    return error


def parse(command, stk, o, envs, ins):
    com = command.split()
    if com[0] == "push":
        push(command[5:], stk)
    elif com[0] == "pop":
        pop(stk)
    elif com[0] == "add":
        add(stk, envs)
    elif com[0] == "sub":
        sub(stk, envs)
    elif com[0] == "mul":
        mul(stk, envs)
    elif com[0] == "div":
        div(stk, envs)
    elif com[0] == "rem":
        rem(stk, envs)
    elif com[0] == "neg":
        neg(stk, envs)
    elif com[0] == 'bind':
        bind(stk, envs)
    elif com[0] == 'let':
        let(stk, envs)
    elif com[0] == 'end':
        end(stk, envs)
    elif com[0] == 'cat':
        cat(stk, envs)
    elif com[0] == 'and':
        and_(stk, envs)
    elif com[0] == 'or':
        or_(stk, envs)
    elif com[0] == 'not':
        not_(stk, envs)
    elif com[0] == 'equal':
        equal(stk, envs)
    elif com[0] == 'lessThan':
        lessThan(stk, envs)
    elif com[0] == 'if':
        if_(stk, envs)
    elif com[0] == "swap":
        swap(stk)
    elif com[0] == "fun":
        function(stk, envs, com[1], com[2], ins)
    elif com[0] == "inOutFun":
        inoutfunction(stk, envs, com[1], com[2], ins)
    elif com[0] == "call":
        call(stk, envs)
    elif com[0] == "quit":
        quit(stk, o)

def inoutfunction(stk, envs, name, arg, ins):
#    print(envs, '\n\n')
    
    if name == arg or arg == error:
        stk[-1].append(error)
    code = []
    env = []
    command = ins.pop(0)
    while command != 'funEnd':
        code.append(command)
        command = ins.pop(0)
        
    for bind in envs[-1]:
        env.append(bind)
    closure = [env, code, arg]
    envs[-1].append((name, ('inout', closure)))
    stk[-1].append(unit)


def function(stk, envs, name, arg, ins):
#    print(envs, '\n\n')

    if name == arg or arg == error:
        stk[-1].append(error)
    code = []
    env = []
    command = ins.pop(0)
    while command != 'funEnd': #store code
        code.append(command)
        command = ins.pop(0)
        
    for bind in envs[-1]: #store environment
        env.append(bind)
    closure = [env, code, arg]
    envs[-1].append((name, ('closure', closure)))
    stk[-1].append(unit)
#    print(envs, '\n\n')
    

def call(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
    (arg, funName) = (stk[-1].pop(), stk[-1].pop())        
    (ty1, x) = fetch(arg, envs)
    (ty2, y) = fetch(funName, envs)
    if (len(y) != 3 and ty2 in ['closure', 'inout']) or fetch(arg, envs) == error or fetch(funName, envs) == error:
        stk.append(funName)
        stk.append(arg)
        stk.append(error)
#    if y[0] == 'inout':
#        inoutcall(stk, envs, (ty1, x), (ty2, x))
#        envs[-1].append((y[-1], (ty1, x)))
        
    else:
        envs[-1].append((y[-1], (ty1, x)))
        envs.append(y[0])   #push closure environment to stack of environments
        stack = [[]]    #create new stack
        code = y[1] #retrieve code and execute function
        if funName[1] in ['id', 'identity']:
            stack.append((ty1, x))
            top = stack.pop()
            stk[-1].append(top)
        else:
            if ty2 == 'inout':
                for com in range(len(code)):
                    code[com] = code[com].replace(y[-1], arg[1])
                    y[-1] = arg[1]
#                print(code)
            for line in code:
#                print('envs:', envs, '\n')
                if line == 'return':
                    lastStackFrame = stack[-1].pop()
                    stk[-1].append(lastStackFrame)
                    envs.pop()
                    if len(envs[-1]) > 0:
                        envs[-1].pop()
                    break
                parse(line, stack, None, envs, code)
            if ty2 == 'inout':
                for bind in range(len(envs[-2])):
                    if envs[-2][bind][0] == y[-1]:
                        for tie in envs[-1]:
                            if tie[0] == y[-1]:
                              envs[-2][bind] = tie
                envs.pop()
                

def let(stk, envs):
    stk.append([])
    envs.append([])


def end(stk, envs):
    current_stack = stk.pop()
    stk[-1].append(current_stack.pop())
    envs.pop()


def bind(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return
    a = stk[-1].pop()
    (ty1, x) = fetch(a, envs)
    (ty2, y) = stk[-1].pop()
    if ty2 != 'name' or ty1 == 'err':
        stk[-1].append((ty2, y))
        stk[-1].append(a)
        stk[-1].append(error)
        return
    stk[-1].append(unit)
    envs[-1].append((y, (ty1, x)))


def push(value, stk):
    try:
        return stk[-1].append(('int', int(value)))
    except:
        pass
    if value.startswith('"'):
        if all([ord(c) <= 127 for c in value[1:-1]]):
            return stk[-1].append(('str', value[1:-1]))
        else:
            return stk[-1].append(error)
    elif value.startswith(':true:'):
        return stk[-1].append(('bool', True))
    elif value.startswith(':false:'):
        return stk[-1].append(('bool', False))
    elif value.startswith(':error:'):
        return stk[-1].append(error)
    elif isName(value):
        return stk[-1].append(('name', value))
    else:
        return stk[-1].append(error)


def pop(stk):
    if len(stk[-1]) < 1:
        stk[-1].append(error)
        return
    stk[-1].pop()


def add(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return
    (a, b) = (stk[-1].pop(), stk[-1].pop())
    (ty1, x) = fetch(a, envs)
    (ty2, y) = fetch(b, envs)
    if ty1 != 'int' or ty2 != 'int':
        stk[-1].append(b)
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append((ty1, y + x))


def sub(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return
    (a, b) = (stk[-1].pop(), stk[-1].pop())
    (ty1, x) = fetch(a, envs)
    (ty2, y) = fetch(b, envs)
    if ty1 != 'int' or ty2 != 'int':
        stk[-1].append(b)
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append((ty1, y - x))


def mul(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return
    (a, b) = (stk[-1].pop(), stk[-1].pop())
    (ty1, x) = fetch(a, envs)
    (ty2, y) = fetch(b, envs)
    if ty1 != 'int' or ty2 != 'int':
        stk[-1].append(b)
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append((ty1, y * x))


def div(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return
    (a, b) = (stk[-1].pop(), stk[-1].pop())
    (ty1, x) = fetch(a, envs)
    (ty2, y) = fetch(b, envs)
    if ty1 != 'int' or ty2 != 'int' or x == 0:
        stk[-1].append(b)
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append((ty1, y // x))


def rem(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return
    (a, b) = (stk[-1].pop(), stk[-1].pop())
    (ty1, x) = fetch(a, envs)
    (ty2, y) = fetch(b, envs)
    if ty1 != 'int' or ty2 != 'int' or x == 0:
        stk[-1].append(b)
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append((ty1, y % x))


def neg(stk, envs):
    if len(stk[-1]) == 0:
        stk[-1].append(error)
        return
    a = stk[-1].pop()
    (ty1, x) = fetch(a, envs)
    if ty1 != 'int':
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append((ty1, -x))


def cat(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return
    (a, b) = (stk[-1].pop(), stk[-1].pop())
    (ty1, x) = fetch(a, envs)
    (ty2, y) = fetch(b, envs)
    if ty1 != 'str' or ty2 != 'str':
        stk[-1].append(b)
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append((ty1, y + x))


def and_(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return
    a = stk[-1].pop()
    b = stk[-1].pop()
    (ty1, x) = fetch(a, envs)
    (ty2, y) = fetch(b, envs)
    if ty1 != 'bool' or ty2 != 'bool':
        stk[-1].append(b)
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append((ty1, x and y))


def or_(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return
    a = stk[-1].pop()
    b = stk[-1].pop()
    (ty1, x) = fetch(a, envs)
    (ty2, y) = fetch(b, envs)
    if ty1 != 'bool' or ty2 != 'bool':
        stk[-1].append(b)
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append((ty1, x or y))


def if_(stk, envs):
    if len(stk[-1]) < 3:
        stk[-1].append(error)
        return
    x = stk[-1].pop()
    y = stk[-1].pop()
    z = stk[-1].pop()
    (ty1, b) = fetch(z, envs)
    if ty1 != 'bool':
        stk[-1].append(z)
        stk[-1].append(y)
        stk[-1].append(x)
        stk[-1].append(error)
        return
    if b is True:
        stk[-1].append(x)
    else:
        stk[-1].append(y)


def not_(stk, envs):
    if len(stk[-1]) == 0:
        stk[-1].append(error)
        return
    a = stk[-1].pop()
    (ty1, x) = fetch(a, envs)
    if ty1 != 'bool':
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append((ty1, not x))


def lessThan(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return
    (a, b) = (stk[-1].pop(), stk[-1].pop())
    (ty1, x) = fetch(a, envs)
    (ty2, y) = fetch(b, envs)
    if ty1 != 'int' or ty2 != 'int':
        stk[-1].append(b)
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append(('bool', str(y < x).lower()))


def equal(stk, envs):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return
    (a, b) = (stk[-1].pop(), stk[-1].pop())
    (ty1, x) = fetch(a, envs)
    (ty2, y) = fetch(b, envs)
    if ty1 != 'int' or ty2 != 'int':
        stk[-1].append(b)
        stk[-1].append(a)
        stk[-1].append(error)
    else:
        stk[-1].append(('bool', y == x))


def swap(stk):
    if len(stk[-1]) < 2:
        stk[-1].append(error)
        return stk
    x = stk[-1].pop()
    y = stk[-1].pop()
    stk[-1].append(x)
    stk[-1].append(y)


def quit(stk, o):
    out = open(o, 'w')
#    print(stk)
    for (ty, val) in reversed(stk[-1]):
        if ty in ['int', 'name', 'str']:
            out.write(str(val) + '\n')
        elif ty in ['err', 'bool', 'unit']:
            out.write(':' + str(val).lower() + ':' + '\n')
        else:
            out.write(val + '\n')
    out.close()
    return


def interpreter(i, o):
    ins = [line.rstrip() for line in open(i)]  # open the input file and read all lines
    stk = [[]]
    envs = [[]]
    while ins:
        s = ins.pop(0)
        parse(s, stk, o, envs, ins)

