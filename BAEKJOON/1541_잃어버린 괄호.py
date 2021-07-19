problem = input().split('-')

num = []
for p in problem:
    cnt = 0
    tmp = p.split('+')
    for t in tmp:
        cnt += int(t)
    num.append(cnt)

res = num[0]
for n in range(1, len(num)):
    res -= num[n]

print(res)
