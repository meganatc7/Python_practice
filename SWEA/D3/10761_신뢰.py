import sys
sys.stdin = open('data/input.txt','r')
T = int(input())

for t in range(1,T+1):
    btn_list = input().split()
    N = int(btn_list.pop(0))

    Turn = []
    Blue = []
    Orange = []
    # 각각의 Blue가 가야할 버튼 위치 Orange가 가야할 버튼 위치
    # 그리고 버튼을 누를 차례를 리스트에 나눠서 저장
    for i in range(0,N*2,2):
        if btn_list[i] == 'B':
            Blue.append(int(btn_list[i+1]))
            Turn.append(btn_list[i])
        else:
            Orange.append(int(btn_list[i+1]))
            Turn.append(btn_list[i])

    # B와 O 로봇의 위치를 표현할 변수들
    B = 1
    O = 1
    time = 0

    # 차례가 계속 있을 동안에는
    while Turn:
        # 만약 차례가 B인 경우
        if Turn[0] == 'B':
            # B를 목표지점 까지 계속 이동
            if Blue[0] > B:
                B += 1
            elif Blue[0] < B:
                B -= 1
            # 목표지점에 도달했다면, 버튼을 눌렀다는 의미로
            # 목표지점의 위치(숫자)와 차례를 리스트에서 pop
            elif Blue[0] == B:
                Blue.pop(0)
                Turn.pop(0)
            # B가 움직이는 와중에는 O도 꾸준히 움직임, 다만 목적지에 도착햇을때는 기다림
            if Orange:
                if Orange[0] > O:
                    O += 1
                elif Orange[0] < O:
                    O -= 1
        # 차례가 O이면 위와 같은 과정을 반복
        elif Turn[0] == 'O':
            if Orange[0] > O:
                O += 1
            elif Orange[0] < O:
                O -= 1
            elif Orange[0] == O:
                Orange.pop(0)
                Turn.pop(0)
            if Blue:
                if Blue[0] > B:
                    B += 1
                elif Blue[0] < B:
                    B -= 1
        
        time += 1 # 움직이거나 버튼 누를때 마다 1타임씩 증가
    print('#{} {}'.format(t,time))
