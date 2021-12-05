from functools import reduce

def red(acc, l):
    split = list(l)
    for i in range(len(acc)):
        acc[i] += split[i]
    return acc

def mp(str):
    return reduce(lambda acc,s: acc + int(s), list(str), 0)

def find(fn, lines):
    rest = lines
    for i in range(len(lines[0]) -1):
        acc = list(reduce(red, rest, ['' for _ in range(len(lines[0]) -1)]))
        counts = list(map(mp, acc))
        count = counts[i]
        b = fn(count - (len(rest) - count))

        rest = [l for l in rest if l[i] == b]
        if len(rest) == 1:
            return rest[0]

    return rest[0]



with open('input', 'r') as input:
    lines = input.readlines()
    oxy = find(lambda a: '1' if a >= 0 else '0', lines)
    co2 = find(lambda a: '1' if a < 0 else '0', lines)
    print(int(oxy, 2) * int(co2, 2))

