file = open('day08/day08.in', 'r')
lines = file.readlines()
file.close()

text = ''.join(lines).split('\n')

g = {}

for r,line in enumerate(text):
    for c,val in enumerate(line):
        if val != '.':
            if val not in g: g[val] = []
            g[val].append((r,c))

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

ans = set()
for key in g:
    group = g[key]
    for i in range(len(group)):
        for j in range(i+1,len(group)):
            if i == j: continue
            r1, c1 = group[i]
            r2, c2 = group[j]
            dr = r1 - r2
            dc = c1 - c2
            ndr = dr // gcd(dr, dc)
            ndc = dc // gcd(dr, dc)
            x, y = r1, c1
            while 0 <= x < len(text) and 0 <= y < len(text[0]): 
                ans.add((x, y))
                x += ndr
                y += ndc
            x, y = r2, c2
            while 0 <= x < len(text) and 0 <= y < len(text[0]):
                ans.add((x, y))
                x -= ndr
                y -= ndc
print(len(ans))