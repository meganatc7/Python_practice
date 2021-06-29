import sys

K, N = map(int, input().split())
lst = [int(sys.stdin.readline()) for _ in range(K)]
st = 1
ed = min(lst)

while st <= ed:
    mid = (st + ed) // 2
    cnt = 0
    print(st, ed)
    for i in range(len(lst)):
        cnt += lst[i] // mid

    if cnt >= N:
        st = mid + 1
    else:
        ed = mid - 1

print(ed)