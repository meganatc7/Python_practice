N, M = map(int, input().split())
never_heard = {}
res = []
for n in range(N):
    name = input()
    never_heard[name] = 1
for m in range(M):
    name = input()
    if never_heard.get(name):
        res.append(name)

res.sort()
print(len(res))
for r in res:
    print(r)