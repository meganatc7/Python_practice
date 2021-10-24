N, K = map(int, input().split())


ans = 0
while bin(N).count('1') > K:
    plus = 2 ** bin(N)[::-1].index('1')
    ans += plus
    N += plus
print(ans)