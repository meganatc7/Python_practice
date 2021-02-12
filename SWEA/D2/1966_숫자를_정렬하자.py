T = int(input())

for t in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))

    maxV = 0
    for i in num_list:
        if i > maxV:
            maxV = i

    counting = [0] * (maxV+1)
    result = [0] * N

    for i in num_list:
        counting[i] += 1

    for i in range(1, len(counting)):
        counting[i] += counting[i-1]
    
    for i in range(N-1, -1, -1):
        result[counting[num_list[i]]-1] = str(num_list[i])
        counting[num_list[i]] -= 1
    
    print(f'#{t} {" ".join(result)}')
