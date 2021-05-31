import math
def solution(progresses, speeds):
    answer = []
    time = []

    for i in range(len(progresses)):
        tmp = math.ceil((100 - progresses[i]) / speeds[i])
        time.append(tmp)

    n = time[0]
    cnt = 0
    for t in range(len(time)):
        if time[t] > n:
            answer.append(cnt)
            cnt = 0
            n = time[t]
        cnt += 1
    answer.append(cnt)

    return answer

solution([93, 30, 55],[1, 30, 5])