T = int(input())

for t in range(1,T+1):
    D, L, N = map(int,input().split())
#DL/100(N*(N-1)/2)
    total_D = 0

    for n in range(N):
        #new_D = int(D * (1 + n*(L/100)))
        new_D = int((n * (L / 100)+1) * D)
        total_D += new_D

    print('#{} {}'.format(t,total_D))