import sys
sys.stdin = open('data/sample_input7.txt', 'r')

def bin(s,e,target,cnt):
    middle = (s + e) // 2
    if middle == target:
        res.append(cnt)
    else:
        if target > middle:
            bin(middle, e, target, cnt+1)
        elif target < middle:
            bin(s, middle, target, cnt+1)



T = int(input())
for t in range(1,T+1):
    P, A, B = map(int,input().split())
    res = []
    bin(1,P,A,0)
    bin(1,P,B,0)
    ans = 0
    if res[0] > res[1]:
        ans = 'B'
    elif res[0] < res[1]:
        ans = 'A'

    print('#{} {}'.format(t, ans))

# T = int(input())
#
# for t in range(1, T + 1):
#     l, r, c = map(int, input().split())
#     # book = list(range(l+1))
#     result = []
#     for key in [r, c]:
#         start = 1
#         end = l
#         cnt = 0
#
#         while start <= end:
#             middle = (start + end) // 2
#             if key == middle:
#                 break
#             elif key > middle:
#                 start = middle
#             else:
#                 end = middle
#             cnt += 1
#
#         result.append(cnt)
#
#     if result[0] < result[1]:
#         print('#{} A'.format(t))
#     elif result[0] > result[1]:
#         print('#{} B'.format(t))
#     else:
#         print('#{} 0'.format(t))