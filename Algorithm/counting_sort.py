sample = [1, 2, 2, 4, 5, 3, 3, 5]
cnt = [0] * 6
result = [0] * len(sample)

for i in range(len(sample)):
    cnt[sample[i]] += 1

for i in range(1,len(cnt)):
    cnt[i] += cnt[i-1]

for i in range(len(sample)-1, -1, -1):
    result[cnt[sample[i]] - 1] = sample[i]
    cnt[sample[i]] -= 1

print(result)