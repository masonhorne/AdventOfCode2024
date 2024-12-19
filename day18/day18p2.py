file = open('day18/day18.in', 'r')
lines = file.readlines()
file.close()

n = 70
coords = []
for line in lines:
    x, y = map(int, line.strip().split(','))
    coords.append((x, y))
g = dict()

def solve():
    dirs = [-1, 0, 1, 0, -1]
    d = dict()
    q = [(0, 0, 0)]
    while q:
        x, y, s = q.pop(0)
        if (x, y) in d and d[(x, y)] <= s: continue
        d[(x, y)] = s
        for i in range(4):
            nx, ny = x + dirs[i], y + dirs[i + 1]
            if 0 <= nx <= n and 0 <= ny <= n and (nx, ny) not in g: q.append((nx, ny, s + 1))
    return d

l, r = 0, len(coords) - 1
ans = None
while l <= r:
    m = (l + r) // 2
    g = {coords[i]: 1 for i in range(m + 1)}
    d = solve()
    if (n, n) in d:l = m + 1
    else:
        ans = coords[m]
        r = m - 1
print(','.join(map(str, ans)))