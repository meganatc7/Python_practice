T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    res = 0
    for a in A:
        s = 0
        e = len(B) - 1
        cnt = -1
        while s <= e:
            mid = (s + e) // 2
            if a <= B[mid]:
                e = mid - 1
            else:
                cnt = mid
                s = mid + 1

        res += (cnt + 1)

    print(res)