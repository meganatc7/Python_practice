# sample = [7,55,12,42,78]
sample = list(map(int,input().split()))
cnt_1 = 0
cnt_2 = 0
# 내가 짠 코드
for i in range(len(sample)-1):
    for j in range(i+1, len(sample)):
        cnt_1 += 1
        if sample[i] > sample[j]:
            sample[i], sample[j] = sample[j], sample[i]

print(sample)


# 교재
for i in range(len(sample)-1, 0, -1):
    for j in range(0, i):
        cnt_2 += 1
        if sample[j] > sample[j+1]:
            sample[j], sample[j+1] = sample[j+1], sample[j]

print(cnt_1, cnt_2)