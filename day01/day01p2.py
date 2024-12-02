file = open('day01/day01.in', 'r')
lines = file.readlines()
file.close()
l1, l2 = [], []

for line in lines:
    x,y = map(int, line.split())
    l1.append(x)
    l2.append(y)

mp = dict()
for i in l2:
    mp[i] = mp.get(i, 0) + 1

ans = sum(i * mp.get(i, 0) for i in l1)
print(ans)