T = int(input())

for t in range(1,T+1):
    NxM = list(map(int,input().split()))
    N = NxM[0]
    M = NxM[1]
    word = '1' * M # 글자의 수
    puzzle = [] # puzzle 판 저장할 빈 리스트
    count = 0 # 칸 수에 맞는 글자수가 몇번인지 셀 카운트

    for n in range(N): # puzzle 만드는 반복문
        num = list(map(str,input().split()))
        puzzle.append(num)

    # 퍼즐에서 y축 고정 x 축으로 순회하면서
    # line이라는 변수에 문자열로 담고
    # 그 문자열을 0으로 짤라 리스트를 만들어서
    # 해당 리스트 안에 글자수가 딱 매칭되는게 몇개있는지 카운트
    for y in range(len(puzzle)): 
        line = ''
        for x in range(len(puzzle)):
            line += puzzle[y][x]
        for i in line.split('0'):
            if i == word:
                count += 1
    
    # 마찬가지로 x축 고정 y 축으로 순히하면서 위 과정 반복
    for x in range(len(puzzle)):
        line = ''
        for y in range(len(puzzle)):
            line += puzzle[y][x]
        for i in line.split('0'):
            if i == word:
                count += 1

    print(f'#{t} {count}')