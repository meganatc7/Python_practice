T = int(input())

for t in range(1,T+1):
    N = int(input())
    speed = 0
    car = 0
    for n in range(N):
        command = list(map(int,input().split()))
        if command[0] == 1: # 커맨드가 가속인 경우
            speed += command[1] # 해당 속도를 스피드에 더해주고
            car += speed # 그 스피드 만큼 이동
        elif command[0] == 2: # 커맨드가 감속인 경우
            speed -= command[1] # 해당 속도를 스피드에서 빼주고(감속)
            if speed < 0: # 속도가 음수는 될 수 없으니까
                speed = 0 # 음수일 경우에는 0으로
            car += speed # 그리고 그 스피드만큼 차 이동
        else:
            car += speed # 커맨드가 0인 경우 원래 속도로 이동
    print('#{} {}'.format(t,car))
    
