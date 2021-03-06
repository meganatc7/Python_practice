def powerset(idx):
    global cnt
    if idx == N:
        total = 0
        for i in range(N):
            if sel[i]:
                total += nums[i]
        if total == S and sum(sel) != 0:
            cnt = cnt + 1
    else:
        sel[idx] = 0
        powerset(idx+1)
        sel[idx] = 1
        powerset(idx+1)



N, S = map(int,input().split())
nums = list(map(int,input().split()))
sel = [0] * N
cnt = 0
powerset(0)
print(cnt)