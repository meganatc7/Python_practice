import sys
sys.stdin = open('data/data2.txt', 'r')

def bfs(s, g):
    cnt = 0
    qu = []
    qu.append(s)
    chk[s] = 1
    while qu:
        cnt += 1
        for _ in range(len(qu)):
            s = qu.pop(0)
            for w in GA[s]:
                if not chk[w]:
                    if w == g: return cnt
                    qu.append(w)
                    chk[w] = 1
    return 0


for t in range(1,int(input())+1):
    V, E = map(int, input().split())
    GA = [[] for _ in range(V+1)]
    chk = [0] * (V+1)
    for e in range(E):
        a, b = map(int, input().split())
        GA[a].append(b)
        GA[b].append(a)
    S, G = map(int, input().split())



    print('#{} {}'.format(t,bfs(S,G)))