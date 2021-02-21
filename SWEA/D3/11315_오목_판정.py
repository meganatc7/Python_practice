T = int(input())

for t in range(1,T+1):
    N = int(input())

    game = []
    
    # 오목판 만들기
    for n in range(N):
        input_data = input()

        tmp = []
        for j in range(len(input_data)):
            tmp.append(input_data[j])
        game.append(tmp)

    width = False
    height = False
    cross = False
    # 가로 검증
    for i in range(len(game)):
        cnt_w = 0
        cnt_h = 0
        for j in range(len(game)):
            # 가로 검증
            if game[i][j] == 'o':
                cnt_w += 1
            else:
                cnt_w = 0
            if cnt_w == 5:
                width = True
                break
            
            # 세로 검증
            if game[j][i] == 'o':
                cnt_h += 1
            else:
                cnt_h = 0
            if cnt_h == 5:
                height = True
                break

    # 대각선(->) 검증
    for i in range(len(game)-1, -1, -1):
        cnt_1 = 0
        cnt_2 = 0
        for j in range(len(game)-i):
            #1
            if game[j][i+j] == 'o':
                cnt_1 += 1
            else:
                cnt_1 = 0
            if cnt_1 == 5:
                cross = True
                break
            
            #2
            if game[i+j][j] == 'o':
                cnt_2 += 1
            else:
                cnt_2 = 0
            if cnt_2 == 5:
                cross = True
                break

    # 대각선(<-) 검증
    for i in range(len(game)):
        cnt_3 = 0
        for j in range(i+1):
            #1
            if game[j][i-j] == 'o':
                cnt_3 += 1
            else:
                cnt_3 = 0
            if cnt_3 == 5:
                cross = True
                break
    #2
    for i in range(len(game)):
        cnt_4 = 0
        for j in range(i+1):
            if game[len(game)-1-i+j][len(game)-1-j] == 'o':
                cnt_4 += 1
            else:
                cnt_4 = 0
            if cnt_4 == 5:
                cross = True
                break

    if width or height or cross:
        print('#{} YES'.format(t))
    else:
        print('#{} NO'.format(t))