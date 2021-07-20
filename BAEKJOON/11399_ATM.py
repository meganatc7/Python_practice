N = int(input())
line = list(map(int, input().split()))

line.sort()

res = 0
for i in range(1,N+1):
    for j in range(i):
        res += line[j]

print(res)