import itertools

N, K = map(int,input().split())
nums = list(map(int,input().split()))


cnt = 0
for kit in list(itertools.permutations((nums))):
    samdae = 500
    for k in kit:
        samdae = samdae - K + k
        if samdae < 500:
            break
    if samdae > 500:
        cnt += 1

print(cnt)