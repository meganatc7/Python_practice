def hunt(a,b):
    global ans_sheep, ans_wolf
    sheep = 0
    wolf = 1
    st = []

    st.append((a,b))
    chk[a][b] = 1
    while st:
        r, c = st.pop()
        for d in range(4):
            nr = r + dir[d][0]
            nc = c + dir[d][1]
            if 0 <= nr < R and 0 <= nc < C and chk[nr][nc] == 0:
                if yard[nr][nc] == '#': continue
                elif yard[nr][nc] == 'o':
                    sheep += 1
                elif yard[nr][nc] == 'v':
                    wolf += 1
                st.append((nr,nc))
                chk[nr][nc] = 1
    if sheep > wolf:
        ans_sheep += sheep
    else:
        ans_wolf += wolf


R, C = map(int, input().split())
yard = list(list(input()) for _ in range(R))
chk = [([0] * C) for _ in range(R)]
dir = [[-1,0],[1,0],[0,1],[0,-1]]
ans_sheep = 0
ans_wolf = 0

for i in range(R):
    for j in range(C):
        if yard[i][j] == 'v' and chk[i][j] == 0:
            hunt(i,j)
print(ans_sheep, ans_wolf)