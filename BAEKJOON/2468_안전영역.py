N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]
maxValue = 0
for x in area:
    for y in x:
        if y > maxValue:
            maxValue = y

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
maxV = 0

for i in range(1, maxValue+1):
    tmp = [[1] * N for _ in range(N)]
    for m in range(N):
        for n in range(N):
            if area[m][n] <= i:
                tmp[m][n] = 0

    cnt = 0
    for a in range(N):
        for b in range(N):
            st = []
            if tmp[a][b] == 1:
                cnt += 1
                st.append((a,b))
                tmp[a][b] = 0
                while st:
                    r,c = st.pop(-1)
                    for d in range(4):
                        nr = r + dir[d][0]
                        nc = c + dir[d][1]
                        if 0 <= nr < N and 0 <= nc < N and tmp[nr][nc] == 1:
                            st.append((nr,nc))
                            tmp[nr][nc] = 0
    if cnt > maxV:
        maxV = cnt

print(maxV)