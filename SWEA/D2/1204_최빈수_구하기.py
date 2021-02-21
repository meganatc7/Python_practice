T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    score = list(map(int,input().split()))
    score_list = [0] * 101

    for i in score:
        score_list[i] += 1

    top_values = []
    
    for j in range(len(score_list)):
        if max(score_list) == score_list[j]:
            top_values.append(j)

    print('#{} {}'.format(t,top_values[-1]))


    
