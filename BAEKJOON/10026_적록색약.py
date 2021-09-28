def challenger(r,c):
    if chk_challenger[r][c]: return
    res[1] += 1
    color = BRD[r][c]
    q = [(r, c)]
    chk_challenger[r][c] = 1
    if color == 'B':
        while q:
            r, c = q.pop(0)
            for d in range(4):
                nr = r + dir[d][0]
                nc = c + dir[d][1]
                if 0 <= nr < N and 0 <= nc < N and chk_challenger[nr][nc] == 0 and BRD[nr][nc] == color:
                    q.append((nr, nc))
                    chk_challenger[nr][nc] = 1
    else:
        while q:
            r, c = q.pop(0)
            for d in range(4):
                nr = r + dir[d][0]
                nc = c + dir[d][1]
                if 0 <= nr < N and 0 <= nc < N and chk_challenger[nr][nc] == 0 and (BRD[nr][nc] == 'R' or BRD[nr][nc] == 'G'):
                    q.append((nr, nc))
                    chk_challenger[nr][nc] = 1

def normal(r,c):
    if chk_normal[r][c]: return
    res[0] += 1
    color = BRD[r][c]
    q = [(r,c)]
    chk_normal[r][c] = 1
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dir[d][0]
            nc = c + dir[d][1]
            if 0 <= nr < N and 0 <= nc < N and chk_normal[nr][nc] == 0 and BRD[nr][nc] == color:
                q.append((nr,nc))
                chk_normal[nr][nc] = 1


N = int(input())
BRD = []
chk_normal = [[0] * N for _ in range(N)]
chk_challenger = [[0] * N for _ in range(N)]
res = [0, 0]
dir = [[-1,0],[0,1],[1,0],[0,-1]]
for n in range(N):
    BRD.append(list(input()))

for i in range(N):
    for j in range(N):
        normal(i,j)
        challenger(i,j)

print(*res)