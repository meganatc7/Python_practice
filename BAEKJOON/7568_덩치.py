N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
rank = [1] * N

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        my_weight = people[i][0]
        my_height = people[i][1]
        your_weight = people[j][0]
        your_height = people[j][1]

        if my_weight < your_weight and my_height < your_height:
            rank[i] += 1
        else:
            continue

print(' '.join(map(str,rank)))

# 3
# 5 4
# 5 3
# 2 3