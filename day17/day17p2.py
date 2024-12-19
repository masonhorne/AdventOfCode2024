file = open('day17/day17.in', 'r')
lines = file.readlines()
file.close()

text = ''.join(lines).strip()
registers, program = text.split('\n\n')
r = dict()
for reg in registers.split('\n'):
    a, seq, v = reg.split()
    r[seq[:-1]] = int(v)
instructions = list(map(int, program.split()[1].split(',')))

def get_op_val(op, a, b, c):
    if op <= 3: return op
    if op == 4: return a
    if op == 5: return b
    if op == 6: return c

def solve(instructions, a, b, c):
    ans = []
    i = 0
    while i < len(instructions):
        ins = instructions[i]
        op = instructions[i + 1]
        op_val = get_op_val(op, a, b, c)
        if ins == 0: a = a >> op_val
        if ins == 1: b ^= op
        if ins == 2: b = op_val % 8
        if ins == 3 and a != 0:
            i = op
            continue
        if ins == 4: b ^=  c
        if ins == 5: ans.append(op_val % 8)
        if ins == 6: b = a >> op_val
        if ins == 7: c = a >> op_val
        i += 2
    return ans

def calc(seq):
    i = seq[0]
    d = 10
    for c in seq[1:]:
        i += (c >> 7) << d
        d += 3
    return i

s = []
for a in range(2 ** 10): s.append(solve(instructions, a, r['B'], r['C'])[0])
dp = [[i] for i in range(2 ** 10) if s[i] == instructions[0]]
for k in instructions[1:]:
    res = []
    for seq in dp:
        cur = seq[-1] >> 3
        for i in range(8):
            if s[(i << 7) + cur] == k: 
                res.append(seq + [(i << 7) + cur])
    dp = res
ans = float('inf')
for seq in dp:
    i = calc(seq)
    if solve(instructions, i, r['B'], r['C']) == instructions: ans = min(ans, i)
print(ans)