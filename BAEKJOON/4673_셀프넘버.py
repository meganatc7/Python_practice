def d(num):
    res = num
    for n in str(num):
        res += int(n)
    if res < 10000:
        memo[res] = 1

memo = [0] * 10001
for i in range(10000):
    d(i)

for m in range(len(memo)-1):
    if memo[m] == 0:
        print(m)