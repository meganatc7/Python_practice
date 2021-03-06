def dfs(depth, sumN):
    global ans

    if depth == N:
        return

    if sumN + seq[depth] == S:
        ans += 1

    dfs(depth + 1, sumN)
    dfs(depth + 1, sumN + seq[depth])


N, S = map(int, input().split())
seq = list(map(int, input().split()))

ans = 0
dfs(0, 0)
print(ans)