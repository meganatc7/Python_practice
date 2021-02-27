N = int(input())
win = []
for n in range(N):
    tmp = [list(map(int,input().split())) for _ in range(2)]
    A = tmp[0][1:]
    B = tmp[1][1:]
    A_lst = [0,0,0,0,0]
    B_lst = [0,0,0,0,0]

    for i in A:
        A_lst[i] += 1
    for i in B:
        B_lst[i] += 1
    winner = ''
    for i in range(4,0,-1):
        if A_lst[i] > B_lst[i]:
            winner = 'A'
            break
        elif A_lst[i] < B_lst[i]:
            winner = 'B'
            break
    if winner:
        win.append(winner)
    else:
        win.append('D')

for i in win:
    print(i)
