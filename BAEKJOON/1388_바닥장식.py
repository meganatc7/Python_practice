def dfs(r, c):
    global count
    chk[r][c] = 1

    if floor[r][c] == '-':
        nr, nc = r, c+1
        if nr < N and nc < M:
            if floor[r][c] == floor[nr][nc]:
                dfs(nr,nc)
            else:
                count += 1
        else:
            count += 1
    else:
        nr, nc = r+1, c
        if nr < N and nc < M:
            if floor[r][c] == floor[nr][nc]:
                dfs(nr,nc)
            else:
                count += 1
        else:
            count += 1


N, M = map(int,input().split())

floor = [list(input()) for _ in range(N)]
chk = [[0] * M for _ in range(N)]
count = 0
for i in range(N):
    for j in range(M):
        if chk[i][j] == 0:
            dfs(i, j)

print(count)