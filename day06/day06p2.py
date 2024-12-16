file = open('day06/day06.in', 'r')
lines = file.readlines()
file.close()
text = ''.join(lines)

start = [-1, -1]
g = text.split('\n')
for r, row in enumerate(g):
    for c, col in enumerate(row):
        if col == '^':
            start = [r, c]

def dfs(g, r, c):
    dirs = [-1, 0, 1, 0, -1]
    dirIdx = 0
    stack = []
    path = set()
    states = set()
    stack.append((r, c, dirIdx))
    while stack:
        r, c, dirIdx = stack.pop()
        if (r, c, dirIdx) in states: return None
        path.add((r, c))
        states.add((r, c, dirIdx))
        nr, nc = r + dirs[dirIdx], c + dirs[dirIdx + 1]
        if nr < 0 or nr >= len(g) or nc < 0 or nc >= len(g[0]): return path
        while g[nr][nc] == '#':
            dirIdx = (dirIdx + 1) % 4
            nr, nc = r + dirs[dirIdx], c + dirs[dirIdx + 1]
        r, c = nr, nc
        stack.append((r, c, dirIdx))

ans = 0
path = dfs(g, start[0], start[1])
for (x, y) in path:
    g[x] = g[x][:y] + '#' + g[x][y+1:]
    if dfs(g, start[0], start[1]) == None: ans += 1
    g[x] = g[x][:y] + '.' + g[x][y+1:]
print(ans)