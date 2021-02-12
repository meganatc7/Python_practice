T = int(input())

for t in range(1,T+1):
    calendar = []

    # 달력만들기
    for i in range(1,13):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            calendar.append([x for x in range(1,32)])
        elif i in [4, 6, 9, 11]:
            calendar.append([x for x in range(1,31)])
        else:
            calendar.append([x for x in range(1,29)])

    M, D, m, d = map(int,input().split())

    cnt = 0
    for i in range(M,m+1):
        if i == m: # 마지막 달인 경우
            for j in range(d): # 마지막 달의 날까지(끝값이니까 -1 필요 없음)
                cnt += 1
        elif i == M: # 첫번째 달인 경우
            for j in range(D-1,len(calendar[i-1])): # 첫 달의 날(인덱스니까 -1)부터 그 달 길이만큼 세기
                cnt += 1                            # 월도 인덱스를 맞춰주기 위해 i-1
        else: # 그 이외의 달인 경우
            for j in range(len(calendar[i-1])): # 1일(인덱스는 0)부터 마지막까지 세줌
                cnt += 1
    
    print('#{} {}'.format(t, cnt))