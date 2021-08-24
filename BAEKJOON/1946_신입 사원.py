import sys

T = int(input())
for t in range(T):
    N = int(input())
    score_list = []
    for n in range(N):
        resume, interview = map(int, sys.stdin.readline().split())
        score_list.append([resume, interview])
    score_list.sort()
    min = score_list[0][1]

    cnt = 1
    for i in range(1,N):
        if min > score_list[i][1]:
            min = score_list[i][1]
            cnt += 1

    print(cnt)