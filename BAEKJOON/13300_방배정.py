N, K = input().split()
N, K  = int(N), int(K)
students = [[],[],[],[],[],[]]
for n in range(N):
    tmp = list(map(int,input().split()))
    if tmp[1] == 1:
        students[0].append(tmp)
    elif tmp[1] == 2:
        students[1].append(tmp)
    elif tmp[1] == 3:
        students[2].append(tmp)
    elif tmp[1] == 4:
        students[3].append(tmp)
    elif tmp[1] == 5:
        students[4].append(tmp)
    else:
        students[5].append(tmp)
room = 0
for grade in students:
    cnt_m = 0
    cnt_w = 0
    for info in grade:
        if info[0] == 1:
            cnt_m += 1
        else:
            cnt_w += 1
    if cnt_m % K:
        room += cnt_m//K + 1
    else:
        room += cnt_m//K
    if cnt_w % K:
        room += cnt_w//K + 1
    else:
        room += cnt_w//K


print(room)
