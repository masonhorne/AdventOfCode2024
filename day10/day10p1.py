file = open('day10/day10.in', 'r')
lines = file.readlines()
file.close()

g = [[c for c in l.strip()] for l in lines]
starts = []
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == '0': starts.append((i, j))

def bfs(g, start):
    q = [start]
    res = set()
    dirs = [-1, 0, 1, 0, -1]
    while len(q) > 0:
        i, j = q.pop(0)
        v = int(g[i][j])
        if(v == 9): res.add((i, j))
        else:
            for dirIdx in range(len(dirs) - 1):
                x, y = i + dirs[dirIdx], j + dirs[dirIdx + 1]
                if 0 <= x < len(g) and 0 <= y < len(g[x]) and int(g[x][y]) == v + 1: q.append((x, y))
    return len(res)

ans = 0
for start in starts: ans += bfs(g, start)
print(ans)