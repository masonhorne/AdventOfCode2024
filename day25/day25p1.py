file = open('day25/day25.in', 'r')
lines = file.readlines()
file.close()

text = ''.join(lines)
bps = text.split('\n\n')
n = len(bps[0].split('\n'))

def calc(bp):
    return [sum(1 for row in bp if row[j] == '#') - 1 for j in range(len(bp[0]))]

locks = []
keys = []
for com in bps:
    bp = com.split('\n')
    if all(c == '#' for c in bp[0]): locks.append(calc(bp))
    else: keys.append(calc(bp))

ans = 0
for lock in locks:
    for key in keys:
        if all(lock[i] + key[i] < n - 1 for i in range(len(lock))): ans += 1      
print(ans)