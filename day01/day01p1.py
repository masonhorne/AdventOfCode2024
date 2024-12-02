file = open('day01/day01.in', 'r')
lines = file.readlines()
file.close()
l1, l2 = [], []

for line in lines:
    x,y = map(int, line.split())
    l1.append(x)
    l2.append(y)

l1.sort()
l2.sort()
ans = sum(abs(l1[i] - l2[i]) for i in range(len(l1)))
print(ans)