T = int(input())

for t in range(1,T+1):
    # 전체 칸 수 N, 파리채 크기 M
    NM = list(map(int,input().split()))
    N = NM[0]
    M = NM[1]
    target = []
    # 전체 칸 수만큼 파리 마리수 적어서 이차원 리스트 만들기
    for n in range(N):
        line = list(map(int,input().split()))
        target.append(line)
    # 점수 기록을 저장할 리스트
    total_score = []
    # x축 y축 모두 해당 길이에서 점수칸 고려하여 길이 조정
    # 예를 들어 전체 길이 5 중 파리채 크기가 2이면 5번이 아닌 4번까지 후려칠 수 있음
    for y in range(N-M+1):
        for x in range(N-M+1):
            sum = 0
            # 해당 칸에서 파리채 크기만큼 파리 잡기 (M크기만큼) > 점수 sum에 계산
            for i in range(M):
                for j in range(M):
                    sum += target[y+i][x+j]
            # sum을 리스트에 저장        
            total_score.append(sum)
    # 그중 제일 높은 스코어 뽑아옴
    print(f'#{t} {max(total_score)}')