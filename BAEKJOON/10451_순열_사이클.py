def DFS():
    visited = [0] * (N+1)
    st = []
    cnt = 0
    for i in range(1,N+1):
        if visited[i] == 1:
            continue
        st.append(i)
        visited[i] = 1
        cnt += 1
        while st:
            v = st.pop(-1)
            for w in G[v]:
                if not visited[w]:
                    st.append(w)
                    visited[w] = 1
    return cnt


T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    arr_s = sorted(arr)

    G = [[] for _ in range(N+1)]

    for i in range(N):
        G[arr[i]].append(arr_s[i])
        #G[arr_s[i]].append(arr[i])

    print(DFS())