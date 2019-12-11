import functools

class IntCode():
    def __init__(self, instr_list, input):
        self.input = input
        self.instr_list = instr_list.copy()

    def __repr__(self):
        return "N: %i, V: %i" % (self.n, self.v)

    def run(self):
        prog = self.instr_list
        pi = 0
        while 1:
            digits = functools.reduce(lambda x, y: x + list(divmod(x.pop(), y)),
                [[prog[pi]]]  + [10**(i + 1) for i in range(4)][::-1])
            op_code = digits[-2] * 10 + digits[-1]
            if op_code in [1,2,5,6,7,8]:
                if digits[2]:
                    a = prog[pi + 1]
                else:
                    a = prog[prog[pi + 1]]
                if digits[1]:
                    b = prog[pi + 2]
                else:
                    b = prog[prog[pi + 2]]
                # add
                if op_code == 1:
                    prog[prog[pi + 3]] = a + b
                    pi += 4
                # multiply
                elif op_code == 2:
                    prog[prog[pi + 3]] = a * b
                    pi += 4
                # jump if true
                elif op_code == 5:
                    if a:
                        pi = b
                    else:
                        pi += 3
                # jump if false
                elif op_code == 6:
                    if not a:
                        pi = b
                    else:
                        pi += 3
                # less than
                elif op_code == 7:
                    prog[prog[pi + 3]] = int(a < b)
                    pi += 4
                # less than
                # equals
                elif op_code == 8:
                    prog[prog[pi + 3]] = int(a == b)
                    pi += 4

            elif op_code == 3:
                prog[prog[pi + 1]] = self.input
                pi += 2
            elif op_code == 4:
                # output
                print(prog[prog[pi + 1]])
                pi += 2
            else:
                return(prog)


test_computer = IntCode([1002,4,3,4,33], 1)
print(test_computer.run())

with open("input","r") as f:
    l = f.readlines()

code = [int(x) for x in l[0].split(',')]
computer = IntCode(code, 1)
computer.run()

jump_test = IntCode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0)
jump_test.run()

print(code)
computer_2 = IntCode(code, 5)
computer_2.run()
