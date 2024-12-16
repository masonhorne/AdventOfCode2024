

file = open('day12/day12.in', 'r')
lines = file.readlines()
file.close()

g = [[c for c in l.strip()] for l in lines]
dirs = [-1, 0, 1, 0, -1]

def bfs(i, j,  g, vis):
    q = [(i, j)]
    a = 0
    p = 0
    peri = dict()
    while q:
        x, y = q.pop(0)
        if (x, y) in vis: continue
        vis.add((x, y))
        a += 1
        for d in range(4):
            nx, ny = x + dirs[d], y + dirs[d + 1]
            if 0 <= nx < len(g) and 0 <= ny < len(g[0]) and g[x][y] == g[nx][ny]: q.append((nx, ny))
            else:
                p += 1
                if (dirs[d], dirs[d + 1]) not in peri: peri[(dirs[d], dirs[d + 1])] = set()
                peri[(dirs[d], dirs[d + 1])].add((x, y))
    s = 0
    for _, v, in peri.items():
        vis2 = set()
        for (x, y) in v:
            if (x, y) not in vis2:
                s += 1
                q2 = [(x, y)]
                while q2:
                    nx, ny = q2.pop(0)
                    if (nx, ny) in vis2: continue
                    vis2.add((nx, ny))
                    for d in range(4):
                        nnx, nny = nx + dirs[d], ny + dirs[d + 1]
                        if (nnx, nny) in v: q2.append((nnx, nny))
    return a * s

vis = set()
ans = 0
for i in range(len(g)):
    for j in range(len(g[i])):
        if (i, j) not in vis:
            ans += bfs(i, j, g, vis)
print(ans)