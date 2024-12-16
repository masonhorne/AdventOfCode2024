file = open('day07/day07.in', 'r')
lines = file.readlines()
file.close()

def dfs(val, idx, vals, t):
    if idx == len(vals): return val == t
    if dfs(val + vals[idx], idx + 1, vals, t): return True
    return dfs(val * vals[idx], idx + 1, vals, t)

ans = 0
for line in lines:
    res, vals = line.strip().split(':')
    vals = list(map(int, vals.strip().split()))
    if dfs(vals[0], 1, vals, int(res)): ans += int(res)
print(ans)