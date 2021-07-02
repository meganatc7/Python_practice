import sys
sys.setrecursionlimit(10000)

def dfs(r, c):
    for d in range(4):
        nr = r + dir[d][0]
        nc = c + dir[d][1]
        if 0 <= nr < N and 0 <= nc < M and farm[nr][nc] == 1:
            farm[nr][nc] = 0
            dfs(nr,nc)


T = int(input())
dir = [[-1,0],[0,1],[1,0],[0,-1]]
for t in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*M for _ in range(N)]
    for k in range(K):
        m, n = map(int, input().split())
        farm[n][m] = 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            if farm[j][i] == 1:
                cnt += 1
                dfs(j,i)
    print(cnt)