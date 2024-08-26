n = int(input())
a = list(map(int, input().split()))
id = [0]*(n+1)
for i, x in enumerate(a):
    id[x]=i
ans = []

for i in range(1, n+1):
    if i != a[i-1]:
        x = id[i]
        id[a[i-1]]=x    
        ans.append((i, id[i]+1))
        a[i-1],a[x]=a[x],a[i-1]
        
print(f"{len(ans)}\n"+"\n".join(f"{i} {j}" for i, j in ans))
        
        
