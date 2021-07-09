T = int(input())
for t in range(1,T+1):
    D, A, B, F = map(int, input().split())

    print('#{} {}'.format(t,(D/(A+B)) * F))