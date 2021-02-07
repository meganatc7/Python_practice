T = int(input())

for t in range(1,T+1):
    
    arg = input().strip()
    score_list = list(map(int,arg.split()))
    for i in range(len(score_list)):
        for j in range(len(score_list)):
            if score_list[i] < score_list[j]:
                score_list[i], score_list[j] = score_list[j], score_list[i]
    
    center_list = score_list[1:9]
    
    sum = 0

    for i in center_list:
        sum += i
    
    avg = sum / len(center_list)
    result = int(round(avg,0))
    print(f'#{t} {result}')


