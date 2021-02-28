def DFS1(v):
    s = []
    visited = [False] * 8

    s.append(v)
    visited[v] = True
    while s:
        v = s.pop(-1)
        print(v, end=' ')
        for w in G[v]:
            if not visited[w]:
                s.append(w)
                visited[w] = True
            
def DFS2(v):
    s = []
    visited = [False] * 8

    s.append(v)
    while s:
        v = s.pop(-1)
        print(v, end=' ')
        visited[v] = True
        for w in G[v]:
            if not visited[w]:
                s.append(w)
                
def DFS3(v):
    visited = [False] * 8
    s = []

    s.append(v)
    visited[v] = True
    while s:
        v = s.pop(-1)
        print(v, end=' ')
        for w in range(len(GA[v])):
            if not visited[w] and GA[v][w] == 1:
                s.append(w)
                visited[w] = True


GA = [
    [0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0],
    [0,1,0,0,1,1,0,0],
    [0,1,0,0,0,0,0,1],
    [0,0,1,0,0,0,1,0],
    [0,0,0,0,1,1,0,1],
    [0,0,0,1,0,0,1,0],
    [0,0,0,1,0,1,0,0]
]
G = [[],[2,3],[1,4,5],[1,7],[2,6],[4,7],[3],[3,5]]
DFS1(1)
print()
DFS2(1)
print()
DFS3(1)