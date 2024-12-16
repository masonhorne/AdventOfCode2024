file = open('day04/day04.in', 'r')
lines = file.readlines()
file.close()

def check_xmas(i, j, lines):
    if i - 1 < 0 or i + 1 >= len(lines): return 0
    if j - 1 < 0 or j + 1 >= len(lines[i]): return 0
    d1 = set([lines[i - 1][j - 1], lines[i + 1][j + 1]])
    d2 = set([lines[i - 1][j + 1], lines[i + 1][j - 1]])
    t = set(["M", "S"])
    if d1.intersection(d2) == t: return 1
    else: return 0

ans = 0
for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        if line[j] == 'A':
            ans += check_xmas(i, j, lines)
print(ans)