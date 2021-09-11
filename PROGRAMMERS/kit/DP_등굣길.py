def solution(m, n, puddles):
    answer = 0
    arr = [[0 for _ in range(m)] for _ in range(n)]

    for pond in puddles:
        arr[pond[1]-1][pond[0]-1] = -1
    arr[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0: continue
            if arr[i][j] != -1:
                if (i - 1) >= 0:
                    if arr[i][j-1] != -1:
                        arr[i][j] += arr[i][j-1]
                if (j - 1) >= 0:
                    if arr[i][j-1] != -1:
                        arr[i][j] += arr[i-1][j]

    print(arr)

    answer = arr[-1][-1]
    return answer


print(solution(4,3,[[2,2]]))