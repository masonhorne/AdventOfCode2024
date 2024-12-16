file = open('day04/day04.in', 'r')
lines = file.readlines()
file.close()

def check_xmas(i, j, xi, xj, lines):
    if i + xi * 3 >= len(lines) or i + xi * 3 < 0: return 0
    if j + xj * 3 >= len(lines[i]) or j + xj * 3 < 0: return 0
    w = ''.join([lines[i + xi][j + xj], lines[i + xi * 2][j + xj * 2], lines[i + xi * 3][j + xj * 3]])
    if w == 'MAS': return 1
    else: return 0

ans = 0
for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        if line[j] == 'X':
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0: continue
                    ans += check_xmas(i, j, dx, dy, lines)
print(ans)