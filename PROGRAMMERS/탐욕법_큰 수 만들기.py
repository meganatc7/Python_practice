def solution(number, k):
    answer = ''
    length = len(number) - k
    result = []
    for n in number:
        while result and n > result[-1]:
            if k > 0:
                result.pop()
                k -= 1
            else:
                break
        result.append(n)

    if k > 0:
        for i in range(k):
            result.pop()

    answer = ''.join(result)

    return answer


print(solution("4177252841",4))