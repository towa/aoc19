def fuel_calc(mass):
    div, _ = divmod(mass, 3)
    fuel = div - 2
    return fuel

with open('input', 'r') as f:
    lines = f.readlines()

fuel = sum([fuel_calc(int(x)) for x in lines])

print(fuel_calc(1969))
print(fuel)


# part 2

def fuel_calc2(mass):
    res = 0
    step = fuel_calc(mass)

    while step > 0:
        res += step
        step = fuel_calc(step)

    return res

fuel2 = sum([fuel_calc2(int(x)) for x in lines])

print(fuel2)

