file = open('day11/day11.in', 'r')
lines = file.readlines()
file.close()
line = ''.join(lines).strip()

def update(mp):
    nmp = dict()
    for key in mp:
        val = mp[key]
        n = len(key)
        if key == "0": nmp["1"] = nmp.get("1", 0) + val
        elif n % 2 == 0:
            n1 = str(int(key[:n // 2]))
            n2 = str(int(key[n // 2:]))
            nmp[n1] = nmp.get(n1, 0) + val
            nmp[n2] = nmp.get(n2, 0) + val
        else:
            k = int(key) * 2024
            nmp[str(k)] = nmp.get(str(k), 0) + val
    return nmp

mp = dict()
for v in line.split():
    mp[v] = mp.get(v, 1)
for k in range(75):
    mp = update(mp)
print(sum(mp.values()))