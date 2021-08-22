def solution(v):
    answer = []
    r = {}
    c = {}
    for spot in v:
        if r.get(str(spot[0])):
            r[str(spot[0])] += 1
        else:
            r[str(spot[0])] = 1

        if c.get(str(spot[1])):
            c[str(spot[1])] += 1
        else:
            c[str(spot[1])] = 1

    for key, value in r.items():
        if value == 1:
            answer.append(int(key))

    for key, value in c.items():
        if value == 1:
            answer.append(int(key))

    return answer
