T = int(input())
count = 0
while count < T:
    count += 1
    problem = input()
    pattern = []
    # 패턴이 10글자 이하이므로 모든 패턴 경우의 수를 고래해서
    # 모든 경우의 수를 pattern에 넣어줌
    for i in range(1,11):
        pattern.append(problem[:i])
    
    # 그 패턴 경우의 수 하나씩 꺼내서 확인
    for i in range(10):
        # 각 패턴들의 길이를 tmp에 저장
        tmp = len(pattern[i])
        # 처음부터 길이만큼, 그리고 그 패턴 이후 또 그 길이만큼 같은지 확인
        if problem[:tmp] == problem[tmp:tmp+tmp]:
            # 같으면 글자수 출력!
            print(f'#{count} {tmp}')
            break
    