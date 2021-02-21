# 사방 탐색
arr = [[1,2,3],
        [4,5,6],
        [7,8,9]]

dt = [[-1,0],[1,0],[0,-1],[0,1]]

for c in range(len(arr)):
    for r in range(len(arr)):
        for i in range(len(dt)):
            nc = c + dt[i][0] 
            nr = r + dt[i][1]
            if nc < 0 or nr < 0: continue
            if nc > len(arr)-1 or nr > len(arr)-1: continue
            print(arr[nc][nr],end=' ')
        print()

# 전치 행렬
arr2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(arr2)):
    for j in range(len(arr2)):
        if i < j:
            arr2[i][j], arr2[j][i] = arr2[j][i], arr2[i][j]

print(arr2)

# 지그재그
arr3 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(arr3)):
    for j in range(len(arr3)):
        print(arr3[i][j + (len(arr3)-1-2*j) * (i % 2)], end=' ')
    print()

# 부분집합
bit = [0,0,0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            print(bit)

# 비트연산으로 부분집합
arr4 = [3,8,4,2,1,9,7]

n = len(arr4)

# 경우의 수 만큼 순회(2의 n승)
for i in range(1<<n):
    # 검증
    for j in range(n):
        # 부분집합이 되는 2의n승의 경우의 수가 i로 차례대로 들어오고
        # 그 경우의 수가 몇번째의 인덱스(j)를 포함하는지 검증
        if i & (1<<j):
            print(arr4[j],end=' ')
        print()