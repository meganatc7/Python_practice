import sys
sys.stdin = open('data/sample_input5.txt', 'r')

def dfs(r, c):
    global res
    if maze[r][c] == '1': return
    if maze[r][c] == '3':
        res = 1
        return
    for d in range(4):
        nr = r + dir[d][0]
        nc = c + dir[d][1]
        if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1' and chk[nr][nc] == 0:
            chk[nr][nc] = 1
            dfs(nr,nc)

for t in range(1,int(input())+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    chk = [[0]*N for _ in range(N)]
    dir = [[-1,0],[0,1],[1,0],[0,-1]]
    res = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                dfs(i,j)
    print('#{} {}'.format(t,res))



# def dfs(r, c):
#     st = []
#     st.append((r,c))
#     visited[r][c] = 1
#     while st:
#         r, c = st.pop()
#         for i in range(4):
#             nr = r + dir[i][0]
#             nc = c + dir[i][1]
#             if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and BRD[nr][nc] != '1':
#                 if BRD[nr][nc] == '3':
#                     return 1
#                 else:
#                     st.append((nr,nc))
#                     visited[nr][nc] = 1
#     return 0
#
# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     BRD = [list(input()) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     dir = [[-1,0],[0,1],[1,0],[0,-1]]
#     for i in range(N):
#         for j in range(N):
#             if BRD[i][j] == '2':
#                 result = dfs(i,j)
#
#     print('#{} {}'.format(t,result))
