import itertools

class IntCode():
    def __init__(self, instr_list, n = 0, v = 0):
        self.n = n
        self.v = v
        self.instr_list = instr_list.copy()
        self.instr_list[1] = self.n
        self.instr_list[2] = self.v

    def __repr__(self):
        return "N: %i, V: %i" % (self.n, self.v)

    def run(self):
        prog = self.instr_list
        pi = 0
        while 1:
            if prog[pi] == 1:
                prog[prog[pi + 3]] = prog[prog[pi + 1]] + prog[prog[pi + 2]]
                pi += 4
            elif prog[pi] == 2:
                prog[prog[pi + 3]] = prog[prog[pi + 1]] * prog[prog[pi + 2]]
                pi += 4
            else:
                break
        return prog[0]


with open('input', 'r') as f:
    lines = f.readlines()
prog = [int(x) for x in lines[0].split(',')]


comb = [IntCode(prog, n, v)
        for (n,v) in list(itertools.product(range(100), range(100)))]

for c in comb:
    x = c.run()
    if  x == 19690720:
        print(100 * c.n + c.v)
