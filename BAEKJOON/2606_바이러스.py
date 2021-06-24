import sys
sys.stdin = open('data/2606.txt', 'r')

from collections import deque

N = int(input())
network = [[] for _ in range(N+1)]
chk = [0] * (N+1)
cnt = 0
for _ in range(int(input())):
    a, b = map(int,input().split())
    network[a].append(b)
    network[b].append(a)

qu = [1]
chk[1] = 1
qu = deque(qu)
while qu:
    a = qu.popleft()
    for i in network[a]:
        if chk[i] == 0:
            chk[i] = 1
            qu.append(i)
            cnt += 1

print(cnt)