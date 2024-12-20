file = open('day20/day20.in', 'r')
lines = file.readlines()
file.close()

text = ''.join(lines)
g = [[ch for ch in line] for line in text.split('\n')]
start = None
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == 'S': start = (i, j)

path = []
q = [start]
vis = set()
dirs = [-1, 0, 1, 0, -1]
while q:
    for k in range(len(q)):
        x, y = q.pop(0)
        if (x, y) in vis: continue
        vis.add((x, y))
        path.append((x, y))
        for i in range(4):
            nx, ny = x + dirs[i], y + dirs[i + 1]
            if nx < 0 or nx >= len(g) or ny < 0 or ny >= len(g[0]) or g[nx][ny] == '#': continue
            q.append((nx, ny))
mp = {path[i]: i for i in range(len(path))}

ans = 0
s = 20
for i in range(len(path)):
    x1, y1 = path[i]
    for dx in range(-s, s + 1):
        for dy in range(-s, s + 1):
            if abs(dx) + abs(dy) <= s:
                nx, ny = x1 + dx, y1 + dy
                if (nx, ny) in mp:
                    x2, y2 = nx, ny
                    diff = abs(x1 - x2) + abs(y1 - y2)
                    save = (mp[(nx, ny)] - i) - diff
                    if save >= 100: ans += 1
print(ans)