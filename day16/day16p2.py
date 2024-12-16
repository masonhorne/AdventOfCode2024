file = open('day16/day16.in', 'r')
lines = file.readlines()
file.close()

text = ''.join(lines).strip()
grid = [[ch for ch in line] for line in text.split('\n')]
start = [-1, -1]
end = [-1, -1]
dirs = [-1, 0, 1, 0, -1]
dirIdx = 1
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = [i, j]
        if grid[i][j] == 'E':
            end = [i, j]

def solve():
   q = []
   state = dict()
   dirIdx = 1
   q.append((start, dirIdx, 0))
   while q:
        pos, dirIdx, c = q.pop(0)
        x, y = pos
        if (x, y, dirIdx) in state and state[(x, y, dirIdx)] <= c: continue
        state[(x, y, dirIdx)] = c
        nx = x + dirs[dirIdx]
        ny = y + dirs[dirIdx + 1]
        if grid[nx][ny] != '#': q.append(([nx, ny], dirIdx, c + 1))
        for i in range(1, 4):
            ndi = (dirIdx + i) % 4
            turns = 0 if i == 0 else (2 if i == 2 else 1)
            q.append(([x, y], ndi, c + 1000 * turns))
   return state

states = solve()
es = None
for i in range(4):
    ndi = (dirIdx + i) % 4
    if es is None or states[es] > states[(end[0], end[1], ndi)]:
        es = (end[0], end[1], ndi)

ans = set()
q = {es}
while q:
    s = q.pop()
    c = states[s]
    x, y, dirIdx = s
    ans.add((x, y))
    dx = dirs[dirIdx]
    dy = dirs[dirIdx + 1]
    if (x - dx, y - dy, dirIdx) in states:
        px, py, pdirIdx = x - dx, y - dy, dirIdx
        pc = states[(px, py, pdirIdx)]
        if pc + 1 == c: q.add((px, py, pdirIdx))
    for i in range(1, 4):
        ndi = (dirIdx + i) % 4
        if (x, y, ndi) in states:
            nc = states[(x, y, ndi)]
            turns = 0 if i == 0 else (2 if i == 2 else 1)
            if nc + turns * 1000 == c: q.add((x, y, ndi))
print(len(ans))