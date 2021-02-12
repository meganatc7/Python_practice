T = int(input())

for t in range(1,T+1):
    
    alpha = []

    N = int(input())
    for n in range(N):
        Ci, Ki = map(str,input().split())
        for i in range(int(Ki)):
            alpha.append(Ci)

    # 총 몇줄이 필요한지 계산
    if len(alpha) % 10:
        line_num = len(alpha) // 10 + 1
    else:
        line_num = len(alpha) // 10
    
    cnt = 0 # alpha 인덱스를 세줄 변수
    result = [] # 최종 값을 담을 리스트
    for i in range(line_num): # 계산한 줄 만큼 반복
        tmp = [] # 임시 리스트
        for j in range(10): # 각 줄에 10개씩만 들어갈 수 있도록
            tmp.append(alpha[cnt]) # alpah에 담긴 알파벳들을 앞에서부터 차례대로 담음
            cnt += 1 #  다음을 위해 인덱스를 느려주고
            if cnt == len(alpha): # 만약 인덱스가 alpha의 길이와 같아지면 break
                break
        result.append(tmp) # 1줄씩 result에 담아줌

    print('#{}'.format(t))
    for i in result:
        for j in i:
            print(j,end='')
        print()