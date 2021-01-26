N = int(input())
                            #1 369를 판별할 변수
num = '369'
                            #2 369 등장 횟수 체크할 변수
cnt = 0

                            #3 1부터 N까지 369게임 시작!
for i in range(1, N+1):
                            #4 번호를 문자형으로 바꿔서 j에 저장
    j = str(i)
                            #5 i가 1한자리 수 일 경우
    if i < 10:
                            #6 i를 문자로 바꾼 j가 369중에 있다면 cnt에 +1
        if j in num:
            cnt += 1
                            #7 i가 2자리 수인 경우
    elif (i >= 10 and i < 100):
                            #8 인덱싱으로 한자리씩 판별
        for y in range(0,2):
                            #9 각각의 자리가 369에 중에 있다면 cnt에 +1
            if (j[y] in num):
                cnt = cnt + 1
                            #10 i가 3자리 수인 경우
    else : 
                            #11 인덱싱으로 한자리씩 판별
        for y in range(0,3):
                            #12 각각의 자리가 369 중에 있으면 cnt에 +1
            if (j[y] in num):
                cnt = cnt + 1
                            #13 만약 cnt가 0보다 크다면 '-'*cnt만큼 출력
    if cnt > 0:
        print('-'*cnt, end = ' ')
                            #14 아니면 그냥 i 출력
    else:       
        print(i, end = ' ')
                            #15 cnt는 0으로 초기화
    cnt = 0

