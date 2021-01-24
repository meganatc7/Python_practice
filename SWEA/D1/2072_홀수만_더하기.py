# 입력값 받아오기
T = int(input())
# 입력값만큼 실행 되기 위한 변수 선언
count = 0

# 입력값 만큼 실행하도록 반복
while count < T:
    # 더한 값 저장할 변수 선언
    sum = 0
    # 입력값 받아오기
    num_list = list(map(int,input().split(' ')))
    # 입력값까지 1씩 증가하며 반복
    for i in num_list:
        # 홀수인경우
        if i % 2:
            # 홀수인 값들을 차례대로 더해줌
            sum += i
    # 횟수 1회씩 
    count += 1
    # 홀수들을 더한 값을 출력
    print(f'#{count} {sum}')