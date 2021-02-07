T = int(input())

for t in range(1,T+1):
    NxM = list(map(int,input().split()))
    N = NxM[0]
    M = NxM[1]
    puzzle = []
    count = 0

    for n in range(N):
        num = list(map(int,input().split()))
        puzzle.append(num)
    

    for y in range(len(puzzle)):
        sum = 0
        for x in range(len(puzzle)):
            if puzzle[y][x] == 1:
                sum += 1
                if sum > M:
                    if puzzle[y][x-1] == puzzle[y][x]:
                        sum = 0
                    else:
                        sum -= 1
            elif puzzle[y][x] == 0 and sum == M:
                continue
            elif puzzle[y][x] == 0:
                sum = 0
                
        if sum == M:
            count += 1

    for x in range(len(puzzle)):
        sum = 0
        for y in range(len(puzzle)):
            if puzzle[y][x] == 1:
                sum += 1
                if sum > M:
                    if puzzle[y][x-1] == puzzle[y][x]:
                        sum = 0
                    else:
                        sum -= 1
            elif puzzle[y][x] == 0 and sum == M:
                continue
            elif puzzle[y][x] == 0:
                sum = 0
                
        if sum == M:
            count += 1

    print(f'#{t} {count}')

