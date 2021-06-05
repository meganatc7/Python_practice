from collections import deque
def solution(n, edge):
    answer = 0

    lst = [0] * (n + 1)

    arr = [[] for _ in range(n+1)]

    for ed in edge:
        arr[ed[0]].append(ed[1])
        arr[ed[1]].append(ed[0])
    print(arr)
    Q = [[1]]
    cnt = 1
    while Q[0]:
        nodes = Q.pop(0)
        tmp = []
        for node in nodes:
            if not lst[node]:
                lst[node] = cnt
                for i in arr[node]:
                    tmp.append(i)
        Q.append(tmp)
        cnt += 1

    answer = lst.count(max(lst))


    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))