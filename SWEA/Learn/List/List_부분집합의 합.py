import sys
sys.stdin = open('data/sample_input5.txt', 'r')

def powerset(idx):
    global N, K, res
    if idx == 12:
        tmp = 0
        if lst.count(1) == N:
            for i in range(12):
                if lst[i] == 1:
                    tmp += i+1
            if tmp == K:
                res += 1
    else:
        lst[idx] = 1
        powerset(idx+1)
        lst[idx] = 0
        powerset(idx+1)

T = int(input())

for t in range(1, T+1):
    lst = [0] * 12
    res = 0
    N ,K = map(int,input().split())
    powerset(0)
    print('#{} {}'.format(t, res))

# T = int(input())
#
# for t in range(1, T + 1):
#
#     A = list(range(1, 13))
#     result = 0
#     N, K = map(int, input().split())
#
#     for i in range(1 << len(A)):
#         cnt = 0
#         total = 0
#         for j in range(len(A)):
#             if i & (1 << j):
#                 total += A[j]
#                 cnt += 1
#         if cnt == N and total == K:
#             result += 1
#
#     print('#{} {}'.format(t, result))