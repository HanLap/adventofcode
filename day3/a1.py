from functools import reduce

def red(acc, l):
    split = list(l)
    for i in range(len(acc)):
        acc[i] += split[i]
    return acc

def mp(str):
    return reduce(lambda acc,s: acc + int(s), list(str), 0)
     

g = ''
e = ''
with open('input', 'r') as input:
    lines = input.readlines()
    length = len(lines)
    acc = reduce(red, lines, ['' for _ in range(12)])
    count = map(mp, acc)
    for b in count:
        if b > length - b:
            g += '1'
            e += '0'
        else:
            g += '0'
            e += '1'

print(int(g, 2) * int(e, 2))

