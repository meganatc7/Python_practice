import sys
sys.stdin = open('data/9367.txt', 'r')

for t in range(int(input())):
    n, m = map(int, input().split())
    cars = {}
    for _ in range(n):
        N, p, q, k = input().split()
        cars[N] = [int(p), int(q), int(k)] # 원가, 렌탈비, 주행비용
    info = []
    for _ in range(m):
        t, S, e, car = input().split()
        info.append([int(t), S, e, car])
    info.sort(key=lambda x : (x[1], x[0]))

    name = ''
    person = {}
    for record in info:
        if record[1] != name:
            if name:
                if tmp[1] != 'r':
                    person[name] = 'INCONSISTENT'
            name = record[1]
            tmp = [name, 'r', 'car']
            person[name] = 0

        if person.get(name) == 'INCONSISTENT': continue

        # 렌탈 시작 판단
        if tmp[1] == 'r' and record[2] != 'p':
            person[name] = 'INCONSISTENT'
            continue
        elif tmp[1] == 'r' and record[2] == 'p':
            tmp[1] = record[2]
            tmp[2] = record[3]
            person[name] += cars[tmp[2]][1]
            continue

        # 렌탈 이후
        # 반납한 경우
        if tmp[1] == 'p' and record[2] == 'r':
            tmp[1] = record[2]
            person[name] += (int(record[3]) * cars[tmp[2]][2])
        # 사고난 경우
        elif tmp[1] == 'p' and record[2] == 'a':
            person[name] += ((int(record[3]) * cars[tmp[2]][0])//100)
        elif tmp[1] == 'p' and record[2] == 'p':
            person[name] = 'INCONSISTENT'

    if tmp[1] != 'r':
        person[name] = 'INCONSISTENT'

    for key, value in person.items():
        print(key, value)