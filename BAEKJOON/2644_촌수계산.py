from collections import deque

n = int(input())
target_a, target_b = map(int, input().split())
m = int(input())

family = [[] for _ in range(n+1)]
chk = [0 for _ in range(n+1)]

def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for i in range(n+1)]
    visit[start] = 1
    while q:
        d = q.popleft()
        for i in family[d]:
            if visit[i] == 0:
                visit[i] = 1
                chk[i] = chk[d] + 1
                q.append(i)

for _ in range(m):
    a, b = map(int,input().split())
    family[a].append(b)
    family[b].append(a)

bfs(target_a)

print(chk[target_b] if chk[target_b] != 0 else -1)