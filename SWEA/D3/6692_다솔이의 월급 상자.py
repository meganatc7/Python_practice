import sys
sys.stdin = open('data/s_input.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N = int(input())

    total = 0
    for n in range(N):
        tmp = 0
        p, x = map(float,input().split())

        tmp = p * x

        total += tmp
    print('#{} {:.6f}'.format(t,round(total,6)))
