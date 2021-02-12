T = int(input())

for t in range(1,T+1):
    sudoku = []
    for i in range(9):
        data = list(map(int,input().split()))
        sudoku.append(data)
    
    x = False
    y = False
    s = False

    # 가로 검증
    for i in range(9):
        if len(list(set(sudoku[i]))) == 9:
            x = True
        else:
            x = False
            break

    # 세로 검증
    for i in range(9):
        list_y = []
        for j in range(9):
            list_y.append(sudoku[j][i])
        if len(list(set(list_y))) == 9:
            y = True
        else:
            y = False
            break
    
    # 3x3 씩 검증
    for i in range(0, 9, 3): # 세로축 기준 좌표
        for j in range(0, 9 ,3): # 가로축 기준 좌표
            list_s = []
            for k in range(0,3):
                for m in range(0,3):
                    list_s.append(sudoku[i+k][j+m])
            if len(list(set(list_s))) == 9:
                s = True
            else:
                s = False

        if s == False:
            break

    if x and y and s:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))
