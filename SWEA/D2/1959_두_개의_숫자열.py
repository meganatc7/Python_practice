def search_max(short, long):
    max_value = -987654321
    for i in range(len(long)-len(short)+1):
        total = 0
        for j in range(len(short)):
            total += short[j] * long[j+i]

        if max_value < total:
            max_value = total

    return max_value

T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if N > M:
        maxV = search_max(B,A)
    else:
        maxV = search_max(A,B)

    print('#{} {}'.format(t, maxV))