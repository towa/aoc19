with open('input', 'r') as f:
    lines = f.readlines()

prog = [int(x) for x in lines[0].split(',')]

prog[1] = 12
prog[2] = 2

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

print(prog[0])

# Part 2


def force(noun, verb, prog):
    p = prog
    p[1] = noun
    p[2] = verb

    pi = 0
    while 1:
        if p[pi] == 1:
            p[p[pi + 3]] = p[p[pi + 1]] + p[p[pi + 2]]
            pi += 4
        elif prog[pi] == 2:
            p[p[pi + 3]] = p[p[pi + 1]] * p[p[pi + 2]]
            pi += 4
        else:
            break
    return p[0]

def brute_force():
    with open('input', 'r') as f:
        lines = f.readlines()

    prog = [int(x) for x in lines[0].split(',')]

    res = 0
    for i in range(100):
        for j in range(100):
            res = force(i, j, prog)
            print(res)
            if res == 5110675:
                return (i,j)

print(brute_force())
