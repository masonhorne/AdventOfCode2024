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

ans = solve(instructions, r['A'], r['B'], r['C'])
print(','.join(map(str, ans)))