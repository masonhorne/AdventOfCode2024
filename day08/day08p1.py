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
            a1 = (r1 + dr,c1 + dc)
            if 0 <= a1[0] < len(text) and 0 <= a1[1] < len(text[0]): ans.add(a1)
            a2 = (r2-dr,c2-dc)
            if 0 <= a2[0] < len(text) and 0 <= a2[1] < len(text[0]): ans.add(a2)
            if abs(dr) % 3 == 0 and abs(dc) % 3 == 0:
                ans.add((r2+dr//3,c2+dc//3))
                ans.add((r2 + (dr // 3) * 2, c2 + (dc // 3) * 2))
print(len(ans))