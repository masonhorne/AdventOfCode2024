file = open('day09/day09.in', 'r')
lines = file.readlines()
file.close()
line = ''.join(lines).strip()

memory = dict()
free_space = dict()
idx = 0

for l in range(len(line)):
    if l % 2 == 0:
        for i in range(int(line[l])):
            memory[idx] = l // 2
            idx += 1
    else:
        free_space[idx] = int(line[l])
        for i in range(int(line[l])):
            memory[idx] = '.'
            idx += 1

n = len(memory)
odd = len(line) % 2 == 1
r = len(line) - 1 if odd else len(line) - 2
offset = 0 if odd else int(line[-1])

while r >= 0:
    total = int(line[r])
    offset += total
    keys = sorted(free_space.keys())
    i = 0
    while i < len(keys) and keys[i] < n - offset + 1:
        space = free_space[keys[i]]
        if space >= total:
            if space - total > 0: free_space[keys[i] + total] = space - total
            del free_space[keys[i]]
            for j in range(total):
                memory[keys[i] + j] = r // 2
                memory[n - offset + j] = '.'
            i = max(keys) - 1
        else: i += 1
    if r > 0: offset += int(line[r - 1])
    r -= 2

ans = 0
for idx in memory.keys():
    id = memory[idx]
    if id != '.': ans += id * idx
print(ans)