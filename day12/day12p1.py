file = open('day12/day12.in', 'r')
lines = file.readlines()
file.close()

g = [[c for c in l.strip()] for l in lines]
dirs = [-1, 0, 1, 0, -1]

def bfs(i, j,  g, vis):
    q = [(i, j)]
    a = 0
    p = 0
    while q:
        x, y = q.pop(0)
        if (x, y) in vis: continue
        vis.add((x, y))
        a += 1
        for d in range(4):
            nx, ny = x + dirs[d], y + dirs[d + 1]
            if 0 <= nx < len(g) and 0 <= ny < len(g[0]) and g[x][y] == g[nx][ny]: q.append((nx, ny))
            else: p += 1
    return a * p

vis = set()
ans = 0
for i in range(len(g)):
    for j in range(len(g[i])):
        if (i, j) not in vis:
            ans += bfs(i, j, g, vis)
print(ans)