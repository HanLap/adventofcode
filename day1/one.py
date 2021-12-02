count = 0
with open('input', 'r') as input:
    fst, snd, trd = (int(input.readline()) for _ in range(3))
    last = fst + snd + trd
    for line in input.readlines():
        fst, snd, trd = (snd, trd, int(line))
        curr = fst + snd + trd
        if curr > last:
            count += 1
        last = curr
print(count)