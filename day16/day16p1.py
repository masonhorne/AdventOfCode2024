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
ans = None
for i in range(4):
    ndi = (dirIdx + i) % 4
    if ans is None or states[ans] > states[(end[0], end[1], ndi)]:
        ans = (end[0], end[1], ndi)
print(states[ans])