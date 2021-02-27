def getValue(curV):
    minV = 987654321
    for i in range(5):
        for j in range(5):
            if minV > arr[i][j] and curV < arr[i][j]:
                minV = arr[i][j]
    return minV

arr = [
    [9,20,2,18,11],
    [19,1,25,3,21],
    [8,24,10,17,7],
    [15,4,16,5,6],
    [12,13,22,23,14]
]

dr = [1,0,-1,0]
dc = [0,1,0,-1]
dir = 0
dst = [[0 for _ in range(5)] for _ in range(5)]

curR = 0
curC = 0
N = 5
curV = 0

for i in range(N * N):
    curV = getValue(curV) # 최소값 받아오기
    dst[curC][curR] = curV # 그 최소값을 초기 위치에 저장하고
    newR = curR + dr[dir] # 새로운 좌표점으로 이동
    newC = curC + dc[dir] # 현재 dir이 0이기 때문에 열1칸 이동 행은 그대로

    # 방향 전환
    if newR < 0 or newR >= N or newC < 0 or newC >= N or dst[newC][newR] != 0:
        dir = (dir + 1) % 4
        newR = curR + dr[dir]
        newC = curC + dc[dir]
    
    curR = newR
    curC = newC


print(dst)