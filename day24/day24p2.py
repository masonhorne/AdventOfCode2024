file = open('day24/day24.in', 'r')
lines = file.readlines()
file.close()
text = ''.join(lines)

nodes, conns = text.split('\n\n')
nodes = nodes.split('\n')
conns = conns.split('\n')

def find(a, b, operator, gates):
    for gate in gates:
        if gate.startswith(f"{a} {operator} {b}") or gate.startswith(f"{b} {operator} {a}") :return gate.split(" -> ").pop()
    return None

ans = []
c0 = None
for i in range(45):
    n = str(i).zfill(2)
    m1, n1, r1, z1, c1 = None, None, None, None, None
    m1 = find(f"x{n}", f"y{n}", "XOR", conns)
    n1 = find(f"x{n}", f"y{n}", "AND", conns)
    if c0:
        r1 = find(c0, m1, "AND", conns)
        if not r1:
            m1, n1 = n1, m1
            ans.extend([m1, n1])
            r1 = find(c0, m1, "AND", conns)
        z1 = find(c0, m1, "XOR", conns)
        if m1 and m1.startswith("z"):
            m1, z1 = z1, m1
            ans.extend([m1, z1])
        if n1 and n1.startswith("z"):
            n1, z1 = z1, n1
            ans.extend([n1, z1])
        if r1 and r1.startswith("z"):
            r1, z1 = z1, r1
            ans.extend([r1, z1])
        c1 = find(r1, n1, "OR", conns)
    if c1 and c1.startswith("z") and c1 != "z45":
        c1, z1 = z1, c1
        ans.extend([c1, z1])
    c0 = c1 if c0 else n1
print(",".join(sorted(ans)))