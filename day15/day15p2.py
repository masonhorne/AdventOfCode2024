file = open('day15/day15.in', 'r')
lines = file.readlines()
file.close()

text = ''.join(lines).strip()
grid, moves = text.split('\n\n')
grid = [[ch for ch in line] for line in grid.split('\n')]
ngrid = []
for row in grid:
    nrow = []
    for ch in row:
        if ch == '#':
            nrow.extend(['#', '#'])
        elif ch == 'O':
            nrow.extend(['[', ']'])
        elif ch == '.':
            nrow.extend(['.', '.'])
        elif ch == '@':
            nrow.extend(['@', '.'])
    ngrid.append(nrow)
grid = ngrid
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
    if dy == 0:
        if grid[x][y] == '.':
            grid[x][y] = '@'
            grid[pos[0]][pos[1]] = '.'
            return [x, y]
        if grid[x][y] == '[' or grid[x][y] == ']':
            q = [(x, y)]
            if grid[x][y] == '[': q.append((x, y + 1))
            else: q.append((x, y - 1))
            move = []
            while len(q) > 0:
                i, j = q.pop(0)
                move.append((i, j))
                if grid[i + dx][j + dy] == '.': continue
                if grid[i + dx][j + dy] == '#': return pos
                if grid[i + dx][j + dy] in '[]':
                    nx = i + dx
                    ny = j + dy
                    q.append((nx, ny))
                    if grid[nx][ny] == '[': q.append((nx, ny + 1))
                    else: q.append((nx, ny - 1))
            moved = set()
            for i in range(len(move) - 1, -1, -1):
                nx, ny = move[i]
                if (nx, ny) in moved: continue
                moved.add((nx, ny))
                grid[nx + dx][ny + dy] = grid[nx][ny]
                grid[nx][ny] = '.'
            grid[x][y] = '@'
            grid[pos[0]][pos[1]] = '.'
            return [x, y]
    else:
        nx = x
        ny = y
        while grid[nx][ny] in '[]':
            nx += dx
            ny += dy
        if grid[nx][ny] == '.':
            for c in range(ny, y, -dy): grid[x][c] = grid[x][c - dy]
            grid[x][y] = '@'
            grid[pos[0]][pos[1]] = '.'
            return [x, y]
    return pos

for mv in moves: pos = move(pos, mv, grid)

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '[':
            ans += i * 100 + j
print(ans)