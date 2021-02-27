C, R = map(int,input().split())
N = int(input())

if N > C*R:
    print(0)

else:
    stage = [[0 for _ in range(C)] for _ in range(R)]

    sr = R - 1
    sc = 0

    d = 0
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    for i in range(1,C*R+1):

        stage[sr][sc] = i

        if i == N:
            break
        
        new_r = sr + dr[d]
        new_c = sc + dc[d]

        if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C or stage[new_r][new_c] != 0:
            d = (d + 1) % 4
            new_r = sr + dr[d]
            new_c = sc + dc[d]
        
        sr = new_r
        sc = new_c

    flag = False
    for i in range(len(stage)):
        y = 0
        for j in stage[i]:
            x = R - i
            y += 1
            if j == N:
                print(x,y)
                flag = True
                break
        if flag:
            break



