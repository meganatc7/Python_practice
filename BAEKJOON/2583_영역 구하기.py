def bfs(i, j):
    q = []
    cnt = 0
    BRD[i][j] = 1
    cnt += 1
    q.append((i,j))
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dir[d][0]
            nc = c + dir[d][1]
            if 0 <= nr < M and 0 <= nc < N and BRD[nr][nc] == 0:
                BRD[nr][nc] = 1
                cnt += 1
                q.append((nr,nc))
    res_width.append(cnt)

M, N, K = map(int, input().split())
BRD = [[0] * N for _ in range(M)]

for k in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly,ry):
        for j in range(lx,rx):
            BRD[i][j] = 1

res = 0
res_width = []
dir = [[-1,0],[0,1],[1,0],[0,-1]]
for i in range(M):
    for j in range(N):
        if BRD[i][j] == 0:
            res += 1
            bfs(i,j)

print(res)
res_width.sort()
print(*res_width)