def BFS(v):
    dir = [[-1,0],[0,1],[1,0],[0,-1]]
    queue = [v]
    visited[v[0]][v[1]] = 1
    while queue:
        r, c = queue.pop(0)
        if r == N and c == M:
            return visited[r][c]
        for i in range(4):
            nr = r + dir[i][0]
            nc = c + dir[i][1]
            if 1 <= nr <= N and 1 <= nc <= M and maze[nr][nc] == '1':
                if visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr,nc))

N,M = map(int,input().split())

tmp1 = [['0'] * (M+1)]
tmp2 = [list('0'+input()) for _ in range(N)]
maze = tmp1 + tmp2
visited = [[0] * (M+1) for _ in range(N+1)]

print(BFS((1,1)))