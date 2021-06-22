import sys
sys.stdin = open('data/4796.txt', 'r')

case = 1
while True:
    L, P, V = map(int,input().split())
    if L == 0 and P == 0 and V == 0: break

    a, b = divmod(V, P)

    print('Case {}: {}'.format(case, L*a + min(b, L)))
    case += 1