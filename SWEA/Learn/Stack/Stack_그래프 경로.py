import sys
sys.stdin = open('data/sample_input2.txt', 'r')

def dfs(s, e):
    global ans
    if s == e:
        ans = 1
        return
    if ans:
         return
    for i in G[s]:
        if chk[i] == 0:
            chk[i] = 1
            dfs(i, e)

T = int(input())
for t in range(1,T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    chk = [0] * (V+1)
    # 경로 저장
    for e in range(E):
        a, b = map(int,input().split())
        G[a].append(b)

    # 출발, 도착 노드
    s, e = map(int,input().split())
    # print(G)
    chk[s] = 1
    ans = 0
    dfs(s, e)
    print('#{} {}'.format(t,ans))


# def dfs(s, g):
#     stack = []
#
#     stack.append(s)
#     visited[s] = True
#     while stack:
#         v = stack.pop(-1)
#         for w in GL[v]:
#             if not visited[w]:
#                 stack.append(w)
#                 visited[w] = True
#     if not visited[g]:
#         return 0
#     return 1
#
#
# T = int(input())
#
# for t in range(1, T + 1):
#     V, E = map(int, input().split())
#     visited = [False] * (V + 1)
#     GL = [[] for i in range(V + 1)]
#
#     for e in range(E):
#         x, y = map(int, input().split())
#         GL[x].append(y)
#
#     S, G = map(int, input().split())
#     result = dfs(S, G)
#
#     print('#{} {}'.format(t, result))
#
