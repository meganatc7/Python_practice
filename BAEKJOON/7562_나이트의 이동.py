knight = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]

T = int(input())
for t in range(T):
    l = int(input())
    chess = [[0] * l for _ in range(l)]
    now_r, now_c = map(int, input().split())
    target_r, target_c = map(int, input().split())
    chess[now_r][now_c] = -1
    chess[target_r][target_c] = 1

    q = [[(now_r, now_c)]]
    cnt = 0
    flag = False
    while q:
        location_lst = q.pop(0)
        cnt += 1
        tmp = []
        for location in location_lst:
            r, c = location
            if chess[r][c] == 1:
                flag = True
                cnt = 0
                break
            for move in knight:
                nr = r + move[0]
                nc = c + move[1]
                if 0 <= nr < l and 0 <= nc < l:
                    if chess[nr][nc] == 1:
                        flag = True
                        break
                    elif chess[nr][nc] == 0:
                        chess[nr][nc] = -1
                        tmp.append((nr,nc))
            if flag: break
        if flag: break
        q.append(tmp)

    print(cnt)
