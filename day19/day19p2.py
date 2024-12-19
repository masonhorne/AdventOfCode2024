file = open('day19/day19.in', 'r')
lines = file.readlines()
file.close()

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children: return False
            node = node.children[c]
        return node.isEnd

text = ''.join(lines)
ps, ds = text.split('\n\n')
ps = ps.strip().split(', ')
ds = ds.split()
t = Trie()
for p in ps: t.insert(p)

ans = 0
for d in ds:
    dp = [0] * (len(d) + 1)
    dp[0] = 1
    for i in range(1, len(d) + 1):
        for j in range(i):
            if t.search(d[j:i]): dp[i] += dp[j]
    ans += dp[len(d)]
print(ans)