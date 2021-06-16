import sys
sys.stdin = open('data/sample_input2.txt', 'r')
T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = list(map(int,input()))

    maxV = 0
    num = 0
    for i in range(10):
        tmp = nums.count(i)
        if tmp >= maxV and num <= i:
            maxV = tmp
            num = i

    print('#{} {} {}'.format(t,num,maxV))


# T = int(input())
#
# def getMax(idx):
#     max = 0
#     for i in idx:
#         if max < i:
#             max = i
#     return max
#
# for t in range(1, T+1):
#     num = int(input())
#     card = [int(x) for x in input()]
#
#     idx = [0] * 10
#
#     for i in range(len(card)):
#         idx[card[i]] += 1
#
#     max = getMax(idx)
#
#     fre = 0
#     for i in range(len(idx)):
#         if idx[i] == max:
#             fre += 1
#
#     if fre == 1:
#         for i in range(len(idx)):
#             if idx[i] == max:
#                 print(f'#{t} {i} {idx[i]}')
#     else:
#         result = 0
#         for i in range(len(idx)):
#             if idx[i] == max:
#                 if i > result:
#                     result = i
#         print(f'#{t} {result} {max}')