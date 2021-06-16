import sys
sys.stdin = open('data/sample_input4.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    paper = [[0]*10 for _ in range(10)]
    cnt = 0
    for n in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                paper[i][j] += color
                if paper[i][j] == 3:
                    cnt += 1
    print('#{} {}'.format(t,cnt))