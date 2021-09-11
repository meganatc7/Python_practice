def solution(numbers):
    answer = ''
    list(map(str,numbers)).sort(reverse=True)
    print(numbers)
    return answer


solution([3, 30, 34, 5, 9])