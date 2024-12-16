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

ans = 0
for page in pages:
    nums = page.strip().split(',')
    if is_valid(nums, mp): ans += int(nums[len(nums) // 2])
print(ans)