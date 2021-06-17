import sys
sys.stdin = open('data/sample_input7.txt', 'r')

def dfs(idx,value):
    global minV
    if minV < value:
        return
    if idx == N:
        if value < minV:
            minV = value
        return
    for i in range(N):
        if chk[i] == 0:
            chk[i] = 1
            dfs(idx+1, value + numbers[idx][i])
            chk[i] = 0


T = int(input())
for t in range(1,T+1):
    N = int(input())
    numbers = [list(map(int,input().split())) for _ in range(N)]

    res = 0
    chk = [0] * N
    minV = 987654321
    dfs(0,0)
    print('#{} {}'.format(t,minV))