# N, K = map(int,input().split())
# temp = list(map(int,input().split()))

# # 첫번째 조건의 합을 maxTemp변수에 저장
# sumTemp = sum(temp[:K])
# maxTemp = sumTemp

# # K가 1이면 그냥 리스트의 맥스값
# if K == 1:
#     maxTemp = max(temp)
# # 아니라면 앞에 한자리 빼고 뒤에 한자리 더하며 검증
# else:
#     for i in range(K,N):
#         sumTemp -= temp[i - K] 
#         sumTemp += temp[i]
#         if sumTemp > maxTemp:
#             maxTemp = sumTemp
# print(maxTemp)

#############################################################
# 윈도우 슬라이딩

N, K = map(int,input().split())
temp = list(map(int,input().split()))

tmp = 0
for i in range(K):
    tmp += temp[i]

maxV = tmp

for i in range(K,N):
    tmp = tmp + temp[i] - temp[i-K]

    if maxV < tmp:
        maxV = tmp
print(maxV)