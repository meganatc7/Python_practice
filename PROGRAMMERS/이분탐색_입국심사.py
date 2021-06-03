def solution(n, times):
    answer = 0
    minute = 1
    while n:
        if minute in times:
            idx = times.index(minute)
            times[idx] *= 2
            n -= 1
        minute += 1
    return minute

print(solution(6, [7,10]))