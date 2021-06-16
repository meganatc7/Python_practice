import sys
sys.stdin = open('data/sample_input2.txt', 'r')

T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    BRD = [list(input()) for _ in range(N)]
    res = ''
    # 가로검증
    for i in range(N):
        for j in range(N-M+1):
            tmp = BRD[i][j:j+M]
            if tmp == tmp[::-1]:
                res = tmp
                break
        if res:
            break
    # 세로검증
    if not res:
        for i in range(N):
            for j in range(N-M+1):
                tmp = ''
                for k in range(M):
                    tmp += BRD[k+j][i]

                if tmp == tmp[::-1]:
                    res = tmp
                    break
            if res:
                break

    print('#{} {}'.format(t,''.join(res)))