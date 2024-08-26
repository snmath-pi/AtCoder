from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))

c = Counter()

for x in a:
    if c[x]%2== 0:
        n-=1
    else:
        n+=1
    c[x]+=1
    
print(n)