N = int(input()) # 보드의 크기
BRD = [[0] * N for _ in range(N)]
K = int(input()) # 사과의 개수
for _ in range(K):
    c, r = map(int,input().split())
    BRD[r-1][c-1] = 1
L = int(input())
direction = []
for _ in range(L):
    tmp = input().split()
    direction.append(tmp)
print(direction)