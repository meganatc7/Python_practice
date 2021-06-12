import sys
sys.stdin = open('data/sample_input3.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    numbers = list(map(int,input().split()))

    tmp = 0
    for i in range(M):
        tmp += numbers[i]

    maxV = tmp
    minV = tmp

    for i in range(M,N):
        tmp = tmp + numbers[i] - numbers[i-M]

        if maxV < tmp:
            maxV = tmp
        if minV > tmp:
            minV = tmp

    print('#{} {}'.format(t, maxV-minV))



# T = int(input())
#
# for test_case in range(1, T + 1):
#
#     a,y = map(int, input().split())
#     x = list(map(int, input().split()))
#
#
#     num = []
#     for i in range(len(x)-y+1):
#         cnt = 0
#         for z in range(i, y+i):
#             cnt += x[z]
#         num += [cnt]
#         num.sort()
#         result = num[len(num)-1] - num[0]
#     print('#{} {}'.format(test_case, result))