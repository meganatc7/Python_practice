# 반대쪽 대각선 대칭
arr = [[1,2,3],
        [4,5,6],
        [7,8,9]]

for i in range(len(arr)):
    for j in range(len(arr)):
        if i < 2 and j < 2:
            arr[i][j], arr[len(arr)-1-j][len(arr)-1-i] = arr[len(arr)-1-j][len(arr)-1-i], arr[i][j]

print(arr)