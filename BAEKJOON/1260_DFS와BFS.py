def DFS(v):
    visited_d[v] = 1
    print(v,end=' ')
    for i in range(1,N+1):
        if (visited_d[i] == 0 and G[v][i] == 1):
            DFS(i)

def BFS(v):
    queue = [v]
    visited_b[v] = 1
    while queue:
        v = queue.pop(0)
        print(v,end=' ')
        for i in range(1,N+1):
            if (visited_b[i] == 0 and G[v][i] == 1):
                queue.append(i)
                visited_b[i] = 1


N,M,V = map(int,input().split())
G = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    G[a][b] = 1
    G[b][a] = 1
visited_b = [0] * (N+1)
visited_d = [0] * (N+1)

DFS(V)
print()
BFS(V)