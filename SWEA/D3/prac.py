import sys
sys.stdin = open('data/input11.txt','r')

TC = int(input())
for t in range(1, TC+1):
    N = int(input())
    arr = list(map(int,input().split()))

    dp = [1 for i in range(N)]

    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print('#{} {}'.format(t,max(dp)))