T = int(input())

for t in range(1, T+1):
    area = int(input())
    square = []
    for i in range(area):
        line = list(map(int,input().split()))
        square.append(line)

    result = [] # 3번 돌린 모양을 각각 담아줄 빈 리스트
    for turn in range(3): # 3번 돌리기
        cube = [] # 1번 돌린 값을 저장할 빈 리스트
        for i in range(len(square)):
            tmp = []
            for j in range(len(square)-1,-1,-1): # 숫자를 밑에서부터 가져와서 빈리스트에 담고 그걸 차례로 cube리스트에 넣어줌
                tmp.append(square[j][i]) # 3x3이면 (2,0) (1,0) (0,0)을 가져와서 리스트에 넣어줌
            cube.append(tmp) # 한번 돌려진 큐브 완성! (계속 돌려진 큐브 모양)
        square = cube # 돌려진 큐브를 다음 한번 더 돌리기위해 square에 저장
        result.append(square) # 최종 결과를 출력하기 위해 result에 저장 (3차원배열)
    
    print('#{}'.format(t))

    for i in range(area): 
        for j in range(3): # 길이가 3인 3차원 리스트를 순회하면서 i번째 2차원 배열을 출력
            print(''.join(map(str,result[j][i])), end=' ')
            if j == 2:
                print()
