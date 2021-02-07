T = int(input())

for t in range(1,T+1):
    # N : 학생 수, K : 구하고자 하는 학생의 번호
    NK = list(map(int,input().split()))
    N = NK[0]
    K = NK[1]

    # 10개의 평점, 인원수만큼 배분(티오)
    # 예) 20명이면 각 평점당 2명씩
    to = N // 10
    # 학생들의 총점을 저장할 리스트
    score_list = []
    # 평점을 판별할 count변수
    count = 0

    # 점수 입력
    for n in range(N):
        score = list(map(int,input().split()))
        total = 0.35 * score[0] + 0.45 * score[1] + 0.2 * score[2] # 총점 계산
        score_list.append(round(total,2)) # 반올림 해서 리스트에 넣어주고
        score_sorted_list = sorted(score_list, reverse=True) # 내림차순 정렬

    K_score = score_list[K-1] # 구하고자 하는 학생 의 점수

    # TO 수만큼 건너 뛰면서 점수 리스트를 슬라이싱
    for i in range(0,N,to):
        count += 1
        # 예) [99,98,97,96...] 10명이면 99 슬라이싱, 98 슬라이싱....
        # K학생의 점수가 해당 슬라이스 범위에 포함되면 그 카운트를 K평점으로 저장
        if K_score in score_sorted_list[i:i+to]:
            K_credit = count
    # K 평점으로 판별!!
    if K_credit == 1:
        print(f'#{t} A+')
    elif K_credit == 2:
        print(f'#{t} A0')
    elif K_credit == 3:
        print(f'#{t} A-')
    elif K_credit == 4:
        print(f'#{t} B+')
    elif K_credit == 5:
        print(f'#{t} B0')
    elif K_credit == 6:
        print(f'#{t} B-')
    elif K_credit == 7:
        print(f'#{t} C+')
    elif K_credit == 8:
        print(f'#{t} C0')
    elif K_credit == 9:
        print(f'#{t} C-')
    elif K_credit == 10:
        print(f'#{t} D0')