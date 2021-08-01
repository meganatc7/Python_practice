N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
target = list(map(int, input().split()))
res = []
for m in range(M):
    s = 0
    e = N

    if target[m] < cards[0] or target[m] > cards[-1]:
        res.append(0)
        continue

    find = 0
    while s <= e:
        mid = (s + e) // 2
        if cards[mid] == target[m]:
            find = 1
            break
        elif cards[mid] < target[m]:
            s = mid + 1
        else:
            e = mid - 1
    if find:
        res.append(1)
    else:
        res.append(0)

print(*res)