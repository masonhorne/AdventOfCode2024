file = open('day21/day21.in', 'r')
lines = file.readlines()
file.close()

text = ''.join(lines)
targets = text.split('\n')

num_keypad = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    'A': (3, 2)
}

dir_keypad = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}

dirs = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def permute(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i, char in enumerate(s):
        for perm in permute(s[:i] + s[i+1:]):
            perms.append(char + perm)
    return perms

def get_paths(s, e, d):
    xd = e[0] - s[0]
    yd = e[1] - s[1]
    ans = ''
    if xd < 0: ans += '^' * abs(xd)
    else: ans += 'v' * xd
    if yd < 0: ans += '<' * abs(yd)
    else: ans += '>' * yd
    paths = set()
    for perm in permute(ans):
        valid = True
        pos = s
        for ch in perm:
            pos = (pos[0] + dirs[ch][0], pos[1] + dirs[ch][1])
            if pos == d: valid = False
        if valid: paths.add(''.join(perm) + 'A')
    if len(paths) == 0: paths.add('A')
    return list(paths)

def dfs(t, d, memo):
    key = (t, d)
    if key in memo: return memo[key]
    avoid = (3, 0) if d == 0 else (0, 0)
    p = num_keypad['A'] if d == 0 else dir_keypad['A']
    ans = 0
    for i in range(len(t)):
        np = num_keypad[t[i]] if d == 0 else dir_keypad[t[i]]
        moves = get_paths(p, np, avoid)
        if d == 2: ans += len(moves[0])
        else: ans += min(map(lambda x: dfs(x, d + 1, memo), moves))
        p = np
    memo[key] = ans
    return ans

ans = 0
for t in targets:
    memo = {}
    ans += dfs(t, 0, memo) * int(t[:-1])
print(ans)