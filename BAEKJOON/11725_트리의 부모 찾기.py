N = int(input())
tree = [[] for _ in range(N+1)]
for n in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

chk = [0] * (N+1)
res = [0] * (N+1)
st = [1]
chk[1] = 1
while st:
    node = st.pop(0)
    for i in tree[node]:
        if chk[i]: continue
        res[i] = node
        st.append(i)
        chk[i] = 1
for i in range(2,len(res)):
    print(res[i])
