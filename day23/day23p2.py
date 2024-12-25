file = open('day23/day23.in', 'r')
lines = file.readlines()
file.close()
text = ''.join(lines)

g = dict()
for line in text.split('\n'):
    u, v = line.split('-')
    if u not in g: g[u] = set()
    g[u].add(v)
    if v not in g: g[v] = set()
    g[v].add(u)

def bron_kerbosch(R, P, X, graph, res):
    if not P and not X: res.append(R)
    else:
        for v in sorted(P):
            bron_kerbosch(R.union({v}), P.intersection(graph[v]), X.intersection(graph[v]), graph, res)
            P.remove(v)
            X.add(v)

R = set()
P = set(g.keys())
X = set()
ans = []
bron_kerbosch(R, P, X, g, ans)
print(','.join(sorted(max(ans, key=len))))