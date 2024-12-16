file = open('day13/day13.in', 'r')
lines = file.readlines()
file.close()

text = ''.join(lines).strip()
machines = text.split('\n\n')

m = []
for machine in machines:
    lines = machine.split('\n')
    x1, y1 = map(lambda coord: int(coord.replace(',', '').replace('X', '').replace('Y', '').replace('+', '')), lines[0].strip().split(' ')[2:])
    x2, y2 = map(lambda coord: int(coord.replace(',', '').replace('X', '').replace('Y', '').replace('+', '')), lines[1].split(' ')[2:])
    tx, ty = map(lambda coord: int(coord.replace(',', '').replace('X', '').replace('=', '').replace('Y', '')), lines[2].split(' ')[1:])
    offset = 10000000000000
    m.append((x1, y1, x2, y2, tx + offset, ty + offset))

def solve(v1, v2, t):
    ax, ay = v1
    bx, by = v2
    tx, ty = t
    b = (ax * ty - ay * tx) / (ax * by - ay * bx)
    a = (tx - bx * b) / ax
    if a.is_integer() and b.is_integer() and a >= 0 and b >= 0: return 3 * int(a) + int(b)
    return -1

ans = 0
for ms in m:
    res = solve((ms[0], ms[1]), (ms[2], ms[3]), (ms[4], ms[5]))
    if res != -1: ans += res
print(ans)