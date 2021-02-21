def bingo():
    # 사회자가 숫자 하나씩 불러주면
    for i in range(len(ans)):
        total = 0
        # 철수의 빙고판을 돌아서 일치하는 번호를 0으로 바꿔주고
        for j in range(len(brd)):
            flag = 0
            for k in range(len(brd)):
                if ans[i] == brd[j][k]:
                    brd[j][k] = 0
                    flag = 1
                    break
            if flag:
                break
            
        # 가로 세로 검증
        for c in range(5):
            sumc = 0
            sumr = 0
            for r in range(5):
                # 가로
                sumc += brd[c][r]
                #세로
                sumr += brd[r][c]
            if sumc == 0:
                total += 1
            if sumr == 0:
                total += 1
        # 대각선 검증
        sum_1 = 0
        for a in range(5):
            sum_1 += brd[a][a]
        if sum_1 == 0:
            total += 1
        sum_2 = 0
        for a in range(5):
            sum_2 += brd[a][4-a]
        if sum_2 == 0:
            total += 1

        if total >= 3:
            return i+1

brd = [list(map(int,input().split())) for _ in range(5)]
ans = []
for _ in range(5):
    for i in list(map(int,input().split())):
        ans.append(i)

result = bingo()

print(result)