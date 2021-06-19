import sys
sys.stdin = open('data/20006.txt','r')

P, M = map(int,input().split())
rooms = []
for p in range(P):
    l, n = input().split()
    if not rooms:
        rooms.append([[int(l),n]])
        continue

    enter = False
    for room in rooms:
        if len(room) < M and room[0][0] - 10 <= int(l) <= room[0][0] + 10:
            room.append([int(l),n])
            enter = True
            break

    if not enter:
        rooms.append([[int(l),n]])

for room in rooms:
    room.sort(key=lambda x:x[1])

for room in rooms:
    if len(room) == M:
        print('Started!')
    else:
        print('Waiting!')
    for lv, name in room:
        print(lv, name)