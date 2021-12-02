d, x, aim = (0, 0, 0)
with open('input', 'r') as input:
    for line in input.readlines():
        match line.split(' '):
            case ['forward', v]:
                x += int(v)
                d += int(v) * aim
            case ['up', v]:
                aim -= int(v)
            case ['down', v]:
                aim += int(v)
print(d * x)