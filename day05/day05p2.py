file = open('day05/day05.in', 'r')
lines = file.readlines()
file.close()

line = ''.join(lines)
sections = line.split('\n\n')
rules = sections[0].split('\n')
pages = sections[1].split('\n')

mp = dict()
for rule in rules:
    x, y = rule.strip().split("|")
    if x not in mp: mp[x] = set()
    mp[x].add(y)

def is_valid(nums, mp):
    vis = set()
    for n in nums:
        for nbr in mp.get(n, set()):
            if nbr in vis: 
                return False
        vis.add(n)
    return True

invalid_pages = []
for page in pages:
    nums = page.strip().split(',')
    if not is_valid(nums, mp): invalid_pages.append(nums)

def top_sort(nums, mp):
    indeg = dict()
    g = dict()
    for node in nums:
        for nbr in mp.get(node, set()):
            if nbr in nums:
                if node not in g: g[node] = []
                g[node].append(nbr)
                indeg[nbr] = indeg.get(nbr, -1) + 1 
    q = [node for node in nums if indeg.get(node, 0) == 0]
    ans = []
    while q:
        node = q.pop(0)
        ans.append(node)
        for nbr in g.get(node, []):
            indeg[nbr] -= 1
            if indeg[nbr] == 0:
                q.append(nbr)
    return ans

ans = 0
for nums in invalid_pages:
    sorted_nums = top_sort(nums, mp)
    ans += int(sorted_nums[len(sorted_nums) // 2])
print(ans)
