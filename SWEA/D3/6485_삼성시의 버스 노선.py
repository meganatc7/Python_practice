import sys
sys.stdin = open('data/s_input2.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    bus = {}
    for n in range(N):
        A, B = map(int,input().split())
        for i in range(A,B+1):
            bus[i] = bus.get(i,0) + 1

    result = []
    P = int(input())
    for p in range(P):
        c = int(input())
        if c in bus:
            result.append(bus[c])
        else:
            result.append(0)

    print('#{} {}'.format(t, ' '.join(map(str,result))))