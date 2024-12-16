file = open('day14/day14.in', 'r')
lines = file.readlines()
file.close()

text = ''.join(lines).strip()
rn = 101
cn = 103
r = []
for line in text.split('\n'):
    p, v = line.split()
    px, py = map(int, p[2:].split(','))
    vx, vy = map(int, v[2:].split(','))
    r.append([px, py, vx, vy])

def update(rs, s):
    x, y, vx, vy = rs
    rs[0] = (x + vx * s) % rn
    rs[1] = (y + vy * s) % cn

i = 0
ans = None
while ans is None:
    d = [['.'] * rn for _ in range(cn)]
    for rs in r:
        x, y, _, _ = rs
        d[y][x] = '*'
        update(rs, 1)
    if any(['********' in ''.join(d[y]) for y in range(cn)]): ans = i
    i += 1
print(ans)