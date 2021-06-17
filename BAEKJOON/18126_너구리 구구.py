import sys
sys.setrecursionlimit(5002)

def dfs(s, far):
    global ans
    flag = 0
    for j in lst[s]:
        if chk[j[0]] == 0:
            flag = 1
    if flag == 0:
        if far > ans:
            ans = far
        return
    for i in lst[s]:
        if chk[i[0]] == 0:
            chk[i[0]] = 1
            dfs(i[0], far+i[1])
            chk[i[0]] = 0

N = int(input())
room_info = sorted([list(map(int,input().split())) for _ in range(N-1)])
lst = [[] for _ in range(N+1)]
for room in room_info:
    lst[room[0]].append([room[1],room[2]])
    lst[room[1]].append([room[0],room[2]])

chk = [0] * (N+1)
ans = 0
chk[1] = 1
dfs(1,0)
print(ans)
