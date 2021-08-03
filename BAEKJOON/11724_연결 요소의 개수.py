N, M = map(int,input().split())
nodes = [[] for _ in range(N+1)]
chk = [0] * (N+1)
for _ in range(M):
    u, v = map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)

res = 0
for n in range(1,N+1):
    if chk[n] == 1: continue
    st = [n]
    chk[n] = 1
    res += 1
    while st:
        w = st.pop()
        for node in nodes[w]:
            if chk[node] == 1: continue
            chk[node] = 1
            st.append(node)

print(res)