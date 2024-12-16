file = open('day15/day15.in', 'r')
lines = file.readlines()
file.close()

text = ''.join(lines).strip()
grid, moves = text.split('\n\n')
grid = [[ch for ch in line] for line in grid.split('\n')]
moves = ''.join(moves.split())
pos = [-1, -1]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            pos = [i, j]

def move(pos, mv, grid):
    dx = 0 if mv == '<' or mv == '>' else -1 if mv == '^' else 1
    dy = 0 if mv == '^' or mv == 'v' else -1 if mv == '<' else 1
    x, y = pos
    x += dx
    y += dy
    nx = x
    ny = y
    while grid[nx][ny] == 'O':
        nx += dx
        ny += dy
    if grid[nx][ny] == '.':
        grid[nx][ny] = 'O'
        grid[x][y] = '@'
        grid[pos[0]][pos[1]] = '.'
        return [x, y]
    return pos

for mv in moves: pos = move(pos, mv, grid)

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'O':
            ans += i * 100 + j
print(ans)