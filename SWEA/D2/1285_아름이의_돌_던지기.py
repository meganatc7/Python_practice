T = int(input())

for t in range(1, T+1):

    N = int(input())

    for n in range(N):
        data = list(map(int,input().split()))
    
    stone = []
    for i in data:
        stone.append(abs(i))
    
    min_value = min(stone)
    players = stone.count(min_value)

    print('#{} {} {}'.format(t,min_value,players))