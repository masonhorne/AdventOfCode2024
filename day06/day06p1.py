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
    stack.append((r, c, dirIdx))
    while stack:
        r, c, dirIdx = stack.pop()
        path.add((r, c))
        nr, nc = r + dirs[dirIdx], c + dirs[dirIdx + 1]
        if nr < 0 or nr >= len(g) or nc < 0 or nc >= len(g[0]): return path
        while g[nr][nc] == '#':
            dirIdx = (dirIdx + 1) % 4
            nr, nc = r + dirs[dirIdx], c + dirs[dirIdx + 1]
        r, c = nr, nc
        stack.append((r, c, dirIdx))

ans = len(dfs(g, start[0], start[1]))
print(ans)