
def solution(operations):
    answer = []

    result = []

    for i in range(len(operations)):
        if result and operations[i] == 'D 1':
            result.pop()
        elif result and operations[i] == 'D -1':
            result.pop(0)
        else:
            a, b = operations[i].split()
            alpha = a
            num = int(b)
            if alpha == 'I':
                result.append(num)
            result.sort()

    if result:
        answer = [result[-1], result[0]]
    else:
        answer = [0,0]

    return answer

print(solution(["I 7","I 5","I -5","D -1"]))