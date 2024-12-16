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

for rs in r:
    update(rs, 100)
ans = 1
ans *= len([rs for rs in r if rs[0] < (rn - 1) // 2 and rs[1] < (cn - 1) // 2])
ans *= len([rs for rs in r if rs[0] < (rn - 1) // 2 and rs[1] > (cn - 1) // 2])
ans *= len([rs for rs in r if rs[0] > (rn - 1) // 2 and rs[1] < (cn - 1) // 2])
ans *= len([rs for rs in r if rs[0] > (rn - 1) // 2 and rs[1] > (cn - 1) // 2])
print(ans)