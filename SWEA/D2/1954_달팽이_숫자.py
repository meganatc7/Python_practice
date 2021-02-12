T = int(input())

for t in range(1,T+1):

    snail = int(input())

    lst = [[0 for i in range(snail)] for i in range(snail)] # 입력값만큼의 NxN 0으로 된 사각형 만들기
    n = 0 # 총 몇번 돌지를 체크
    ans = 1 # 돌면서 숫자를 1, 2, 3, 4, ..... 를 입력해줄 변수
    brk = 1 # 안으로 들어갈수록 공간을 좁게 해주는 변수
    while n != int(round(snail,0)): # 사각형의 크기에 따라 돌아가는 횟수가 정해짐 (3x3 4x4는 2바퀴)
        for i in range(snail): # 제일 윗줄(평범, 한칸씩 오른쪽으로 가면서 ans를 1씩 증가시키며 넣어줌)
            if lst[n][i] == 0: # 조건문으로 해당 칸이 0이라면!!
                lst[n][i] = ans
                ans += 1

        for i in range(snail): # 오른쪽줄 위에서 아래로
            if lst[i][snail-brk] == 0: 
                lst[i][snail-brk] = ans # (사각형 크기에 맞게 안으로 갈수록 brk때문에 작은 사각형이 됨)
                ans += 1

        for i in range(snail-1,-1,-1): # 아래쪽줄 오른쪽에서 왼쪽으로
            if lst[snail-brk][i] == 0:
                lst[snail-brk][i] = ans
                ans += 1

        for i in range(snail-1,-1,-1): # 왼쪽줄 아래에서 위로
            if lst[i][n] == 0:
                lst[i][n] = ans
                ans += 1

        n += 1
        brk += 1
    print('#{}'.format(t))
    for i in lst:
        for j in i:
            print(j, end=' ')
        print()