file = open('day02/day02.in', 'r')
lines = file.readlines()
file.close()
lines = [list(map(int, line.split())) for line in lines]

def valid(line):
    increasing = line[0] < line[1]
    for i in range(len(line) - 1):
        dif = abs(line[i] - line[i + 1])
        if increasing and line[i] >= line[i + 1]: return False
        if not increasing and line[i] <= line[i + 1]: return False
        if dif > 3 or dif < 1: return False
    return True

def valid2(line):
    for i in range(len(line)):
        if valid(line[:i] + line[i + 1:]): return True
    return False

ans = sum(valid2(line) for line in lines)
print(ans)