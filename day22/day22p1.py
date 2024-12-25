file = open('day22/day22.in', 'r')
lines = file.readlines()
file.close()

def mix(x, y): return x ^ y

def prune(x): return x % 16777216

def update(n):
    n = prune(mix(n * 64, n))
    n = prune(mix(n, n // 32))
    n = prune(mix(n, n * 2048))
    return n

text = ''.join(lines)
nums = list(map(int, text.split('\n')))

ans = 0
for n in nums:
    v = n
    for _ in range(2000): v = update(v)
    ans += v
print(ans)