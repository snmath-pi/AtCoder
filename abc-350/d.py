n, m = map(int, input().split())

a = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u-=1;v-=1
    a[u].append(v); a[v].append(u)

tot = 0
vis = [0]*n
def dfs(x):
    stack = [x]
    vis[x] = 1
    cnt = 1
    while stack:
        node = stack.pop()
        for neighbor in a[node]:
            if not vis[neighbor]:
                stack.append(neighbor)
                vis[neighbor] = 1
                cnt+=1
    return cnt

for i in range(n):
    if vis[i] == 0:
        val =dfs(i)
        tot+=val*(val-1)//2
print(tot-m)