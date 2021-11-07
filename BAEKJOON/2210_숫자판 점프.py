def dfs(r, c, number):
    if len(number) == 6:
        if number not in res:
            res.append(number)
        return

    for d in range(4):
        nr = r + dir[d][0]
        nc = c + dir[d][1]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, number + BRD[nr][nc])

BRD = [list(map(str,input().split())) for i in range(5)]
dir = [[-1,0],[0,1],[1,0],[0,-1]]
res = []
for i in range(5):
    for j in range(5):
        dfs(i,j,BRD[i][j])
print(len(res))