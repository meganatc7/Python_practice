def DFS():
    st = []
    dir = [[-1,0],[0,1],[1,0],[0,-1]]
    result = []
    cnt_v = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            if village[i][j] == '1':
                cnt_v += 1
                st.append((i,j))
                cnt += 1
                while st:
                    r,c = st.pop(-1)
                    village[r][c] = 0
                    for d in range(4):
                        nr = r + dir[d][0]
                        nc = c + dir[d][1]
                        if 0 <= nr < N and 0 <= nc < N and village[nr][nc] == '1':
                            st.append((nr,nc))
                            village[nr][nc] = 0
                            cnt += 1
                result.append(cnt)
    result.sort()
    print(cnt_v)
    for i in result:
        print(i)



N = int(input())
village = [list(input()) for _ in range(N)]
DFS()