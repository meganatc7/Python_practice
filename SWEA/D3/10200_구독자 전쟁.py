import sys
sys.stdin = open('data/input5.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N, A, B = map(int,input().split())

    if A >= B:
        max = B
    else:
        max = A

    min = 0
    if N < A + B:
        min = (A + B) - N

    print('#{} {} {}'.format(t, max, min))