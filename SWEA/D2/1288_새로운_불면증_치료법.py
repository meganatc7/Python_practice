T = int(input())

for t in range(1,T+1):
    
    N = int(input())

    sheep = [0] * 10
    cnt = 1

    while True:
        number = str(N * cnt)

        for i in number:
            sheep[int(i)] = 1
        
        if sum(sheep) == 10:
            break
        
        cnt += 1
        
    print('#{} {}'.format(t,N*cnt))
