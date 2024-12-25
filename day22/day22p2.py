file = open('day22/day22.in', 'r')
lines = file.readlines()
file.close()

def mix(x, y): return x ^ y

def prune(x): return x % 16777216

def update(n):
    n = prune(mix(n * 64, n))
    n = prune(mix(n, n // 32))
    n = prune(mix(n, n * 2048))
    return n

text = ''.join(lines)
nums = list(map(int, text.split('\n')))

ans = dict()
for n in nums:
    v = n
    c = v % 10
    ds = []
    for _ in range(2000): 
        v = update(v)
        nc = v % 10
        ds.append(((nc - c), nc))
        c = nc
    vis = set()
    for i in range(len(ds) - 3):
        pt = (ds[i][0], ds[i + 1][0], ds[i + 2][0], ds[i + 3][0])
        if pt not in vis:
            vis.add(pt)
            if pt not in ans: ans[pt] = 0
            ans[pt] += ds[i + 3][1]
print(max(ans.values()))