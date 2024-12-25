file = open('day24/day24.in', 'r')
lines = file.readlines()
file.close()

text = ''.join(lines)
nodes, conns = text.split('\n\n')
nodes = nodes.split('\n')
conns = conns.split('\n')

vs = dict()
for node in nodes:
    u, v = node.split(': ')
    vs[u] = int(v)
n = len(vs)
g = dict()
for conn in conns:
    u, op, v, _, d = conn.split()
    g[d] = (u, v, op)

while len(vs) < len(g) + n:
    for k in g:
        if k in vs: continue
        u, v, op = g[k]
        if u in vs and v in vs:
            if op == 'AND':
                vs[k] = vs[u] & vs[v]
            elif op == 'OR':
                vs[k] = vs[u] | vs[v]
            elif op == 'XOR':
                vs[k] = vs[u] ^ vs[v]
ans = sorted([(k, vs[k]) for k in vs if k[0] == 'z'])
ans = ''.join(str(ans[i][1]) for i in range(len(ans) - 1, -1, -1))
print(int(ans, 2))