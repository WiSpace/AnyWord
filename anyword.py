import re, os, sys

from args import args
from ai import AI

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))

variables = {}
libobj = {}
debug = args.debug

def find_values(text):
    return re.findall(r"\"([^\"]*)\"", text)

path = os.path.dirname(args.path)
fname = os.path.splitext(os.path.basename(args.path))[0]
lib = False

if os.path.exists(awl_name:=os.path.join(path, fname+".awl")):
    lib = awl_name
elif os.path.exists(awl_name:=os.path.join(path, "main.awl")):
    lib = awl_name

if args.libfile:
    lib = args.libfile

func_awl = {}
with open("ai.txt", encoding="utf-8") as f:
    content = f.read()

if lib:
    with open(lib) as f:
        for i in f.readlines():
            i = i.strip()
            lib_now = __import__(i)
            awl_fun = lib_now.__awc__

            libobj[i] = lib_now

            for awl_now in awl_fun:
                for i in awl_now[0]:
                    scontent = []
                    scontent.append(f"{i}\\{awl_now[1]}")
                    content += "\n" + '\n'.join(map(str, scontent))
                func_awl[awl_now[1]] = awl_now[2]
            
AIO = AI(content)
AIO.start()

with open(args.path, encoding="UTF-8") as f:
    code = f.readlines()

class CodeObj:
    def __init__(self, name, vals, string):
        self.name = name
        self.vals = vals
        self.string = string

class PositionableSequenceIterator:
    def __init__(self, sequence):
        self.seq = sequence
        self._nextpos = 0

    @property
    def pos(self):
        pos = self._nextpos
        return 0 if pos is None else pos - 1

    @pos.setter
    def pos(self, newpos):
        if not 0 <= newpos < len(self.seq):
            raise IndexError(newpos)
        self._nextpos = newpos

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.seq[self._nextpos or 0]
        except IndexError:
            raise StopIteration
        finally:
            self._nextpos += 1

whilet = [False, 0]
n = 0
last = 0

def get_val_tp(val):
    if val in list(variables):
        return variables[val]
    try:
        return eval(val)
    except:pass

    return val

itr = PositionableSequenceIterator(code)
for func in itr:
    if func.strip()=="" or func.startswith("//"):continue
    vals = find_values(func)

    if debug:
        print("now is", AIO.get_func(func).split(' ')[0])

    match AIO.get_func(func).split(' ')[0]:
        case "print":
            print(''.join(map(str, [get_val_tp(i) for i in vals])))
        case "var":
            if len(vals)>1:
                variables[vals[0]] = vals[1]
            else:
                variables[vals[0]] = ""
        case "input":
            variables[vals[0]] = input()
        case "whiletrue":
            whilet = [True, itr.pos]
        case "stop":
            last = itr.pos
            if whilet[0]:
                itr.pos = whilet[1]
        case "jump":
            last = itr.pos
            itr.pos = int(get_val_tp(vals[0]))-1
        case "jumpl":
            itr.pos = last+1
        case _:
            tmp = AIO.get_func(func).split(' ')[0]
            
            if tmp in list(func_awl):
                func_awl[tmp](*[get_val_tp(i) for i in vals])

    for key, val in libobj.items():
        for key, val in val.__awvar__.items():
            variables[key] = val
