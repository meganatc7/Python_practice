n = int(input())
numbers = list(map(int,input().split()))
line = [0] * n
for i in range(n):
    for j in range(i, i-numbers[i], -1):
        line[j] = line[j-1]
    line[i-numbers[i]] = i+1

print(' '.join(map(str,line)))