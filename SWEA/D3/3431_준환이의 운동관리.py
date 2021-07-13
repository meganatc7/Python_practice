import sys
sys.stdin = open('data/input8.txt', 'r')

T = int(input())
for t in range(1, T+1):
    min, max, x = map(int,input().split())

    res = 0
    if min > x :
        res = min - x
    elif max < x:
        res = -1
    else:
        res = 0

    print('#{} {}'.format(t, res))