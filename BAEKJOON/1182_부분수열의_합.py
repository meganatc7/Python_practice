# def powerset(idx):
#     global cnt
#     if idx == N:
#         total = 0
#         for i in range(N):
#             if sel[i]:
#                 total += nums[i]
#         if total == S and sum(sel) != 0:
#             cnt = cnt + 1
#     else:
#         sel[idx] = 0
#         powerset(idx+1)
#         sel[idx] = 1
#         powerset(idx+1)
#
#
#
# N, S = map(int,input().split())
# nums = list(map(int,input().split()))
# sel = [0] * N
# cnt = 0
# powerset(0)
# print(cnt)


#########################################################################################
def f(idx, d):
    global res
    if(idx >= n):
        if(s == d):
            res += 1
            return
    else:
        # 원소를 포함하는 경우
        f(idx+1, d+arr[idx])
        # 원소를 포함하지 않는 경우
        f(idx+1, d)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
f(0,0)
# s가 0인, 즉 공집합인 경우에는 정답에서 -1을 해줌
if(s):
    print(res)
else:
    print(res - 1)