import sys
sys.stdin = open('data/sample_input.txt', 'r')
T = int(input())
for t in range(1,T+1):
    K, N, M = map(int,input().split())
    charge = list(map(int,input().split()))

    now = 0
    k = K
    cnt = 0
    while True:

        now += 1
        k -= 1

        if now >= N:
            break

        if k == 0:
            flag = True
            for i in range(now,now-K, -1):
                if i in charge:
                    k = K
                    now = i
                    cnt += 1
                    flag = False
                    break
            if flag:
                cnt = 0
                break

    print('#{} {}'.format(t,cnt))


# T = int(input())
#
# for t in range(1,T+1):
#     K, N, M = map(int,input().split())
#     station = list(map(int,input().split()))
#
#     k = K
#     cnt = 0
#
#     for i in range(1,N+1):
#         k -= 1
#         for j in range(len(station)-1):
#             if i == station[j]:
#                 if i + k < station[j+1]:
#                     k = K
#                     cnt += 1
#         if i == station[len(station)-1]:
#             if i + k < N:
#                 k = K
#                 cnt += 1
#
#         if k == 0 and i != N:
#             cnt = 0
#             break
#     print(f'#{t} {cnt}')



