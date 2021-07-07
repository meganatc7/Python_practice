from collections import deque

def bfs(x):
    global res

    qu.append(x)
    circles[x] = 1
    color = 2
    while qu:
        circle_num = qu.popleft()
        if circles[circle_num] == 1:
            color = 2
        else:
            color = 1
        for i in info[circle_num]:
            if circles[i] == 0:
                circles[i] = color
                qu.append(i)
            else:
                if circles[circle_num] == circles[i]:
                    res = 'impossible'
        if res == 'impossible': break


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    circles = [0] * (n+1)
    info = [[] for k in range(n+1)]
    for i in range(m):
        x, y = map(int, input().split())
        info[x].append(y)
        info[y].append(x)

    res = 'possible'
    qu = deque()
    bfs(1)

    for i in range(n+1):
        if circles[i] == 0:
            bfs(i)

    print(res)