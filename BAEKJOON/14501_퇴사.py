def profit(idx, total):
    global maxV

    if idx >= N or idx+table[idx][0] > N:
        if maxV < total:
            maxV = total
        return

    profit(idx+table[idx][0], total+table[idx][1])
    profit(idx+1,total)


N = int(input())
table = []
maxV = 0
for n in range(N):
    table.append(list(map(int,input().split())))
profit(0,0)
print(maxV)
