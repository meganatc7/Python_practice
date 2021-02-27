N = int(input())
num = list(map(int,input().split()))
line = [0] * N
for i in range(len(num)):
    line = line[:num[i]] + [i+1] + line[num[i]:]

for i in range(N-1,-1,-1):
    print(line[i], end=' ')
