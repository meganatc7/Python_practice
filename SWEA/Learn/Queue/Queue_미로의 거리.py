import sys
sys.stdin = open('data/sample_input2.txt', 'r')

def bfs(r,c):
    q = [(r,c)]
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dir[d][0]
            nc = c + dir[d][1]
            if 0 <= nr < N and 0 <= nc < N and (map[nr][nc] == '0' or map[nr][nc] == '3') :
                if map[nr][nc] == '3':
                    return map[r][c] - 2
                else:
                    map[nr][nc] = int(map[r][c]) + 1
                    q.append((nr,nc))
    return 0


for t in range(1,int(input())+1):
    N = int(input())
    map = [list(input()) for _ in range(N)]
    dir = [[-1,0],[0,1],[1,0],[0,-1]]
    for i in range(N):
        for j in range(N):
            if map[i][j] == '2':
                res = bfs(i,j)
    print('#{} {}'.format(t,res))



# def bfs(r, c):
#     Q = []
#     Q.append((r,c))
#     visited[r][c] = 1
#     while Q:
#         r, c = Q.pop(0)
#         if BRD[r][c] == '3':
#             return visited[r][c] - 2
#         for d in range(4):
#             nr = r + dir[d][0]
#             nc = c + dir[d][1]
#             if 0 <= nr < N and 0 <= nc < N and BRD[nr][nc] != '1' and visited[nr][nc] == 0:
#                 visited[nr][nc] = visited[r][c] + 1
#                 Q.append((nr,nc))
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
#                 result = bfs(i,j)
#     print('#{} {}'.format(t,result))