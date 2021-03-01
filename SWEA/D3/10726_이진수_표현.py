T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    
    ans = '1' * N
    
    if bin(M)[-N:] == ans:
        print('#{} {}'.format(t,'ON'))
    else:
        print('#{} {}'.format(t,'OFF'))