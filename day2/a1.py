d = 0
x = 0
with open('input', 'r') as input:
    for line in input.readlines():
        split = line.split(' ')
        match split:
            case ['up', v]:
                d -= int(v)
            case ['down', v]:
                d += int(v)
            case ['forward', v]:
                x += int(v)
print(d * x)