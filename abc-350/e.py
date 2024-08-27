from collections import Counter, deque

n, a, x, y = map(int, input().split())
f = Counter()
f[0] = 0

stack = deque([n])

while stack:
    val = stack.pop()
    if val in f:
        continue

    if val == 0:
        f[val] = 0
        continue

    min_cost = float('inf')

    if val / a not in f:
        stack.append(val / a)
    else:
        min_cost = f[val / a] + x

    for i in range(2, 7):
        if i >= a:
            if val / i not in f:
                stack.append(val / i)
            else:
                min_cost = min(min_cost, f[val / i] + y)

    f[val] = min_cost

print(f[n])
