import sys
sys.stdin = open('data/16956.txt', 'r')

def bfs(r,c):
    global ans
    for d in range(4):
        nr = r + dir[d][0]
        nc = c + dir[d][1]
        if 0 <= nr < R and 0 <= nc < C:
            if farm[nr][nc] == 'S':
                ans = 0
                return
            elif farm[nr][nc] == '.' or farm[nr][nc] == 'D':
                farm[nr][nc] = 'D'

R, C = map(int, input().split())
farm = [list(input()) for _ in range(R)]
dir = [[-1,0],[0,1],[1,0],[0,-1]]
ans = 1

for i in range(R):
    for j in range(C):
        if farm[i][j] == 'W':
            bfs(i,j)
            if ans == 0:
                break
    if ans == 0:
        break

if ans == 0:
    print(ans)
else:
    print(ans)
    for f in farm:
        print(''.join(f))