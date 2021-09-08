n = int(input())
m = int(input())
friends = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

res = [1]
for f in friends[1]:
    res.append(f)
    for k in friends[f]:
        res.append(k)

print(len(list(set(res))) - 1)