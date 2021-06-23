import sys
sys.stdin = open('data/14503.txt', 'r')


N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]
dir = [[0,-1],[-1,0],[0,1],[1,0]]
back = [[1,0],[0,-1],[-1,0],[0,1]]
cnt = 0

st = [(r, c, d)]

while st:
    r, c, d = st.pop()
    if room[r][c] == 0:
        cnt += 1
        room[r][c] = 2

    tmp = 0
    for i in range(4):
        nr = r + dir[d][0]
        nc = c + dir[d][1]

        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            st.append((nr, nc, (d+3)%4))
            break
        if room[nr][nc] == 1 or room[nr][nc] == 2:
            tmp += 1
        d = (d+3) % 4

    if tmp == 4 and room[r + back[d][0]][c + back[d][1]] == 2:
        st.append((r + back[d][0], c + back[d][1], d))
    elif tmp == 4:
        break

print(cnt)