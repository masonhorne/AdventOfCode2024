file = open('day03/day03.in', 'r')
lines = file.readlines()
file.close()

line = ''.join(lines)

def get_num_opt(line, i, is_first):
    num = ''
    while line[i] != (',' if is_first else ')'):
        if not line[i].isdigit(): return None
        num += line[i]
        i += 1
    return num

ans = 0
for i in range(len(line) - 4):
    if line[i:i+4] == "mul(":
        d1 = get_num_opt(line, i + 4, True)
        if d1 == None: continue
        d2 = get_num_opt(line, i + 4 + len(d1) + 1, False)
        if d2 == None: continue
        ans += int(d1) * int(d2)
print(ans)