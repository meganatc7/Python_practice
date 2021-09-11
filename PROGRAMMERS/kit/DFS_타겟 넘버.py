def solution(numbers, target):
    answer = 0

    def dfs(idx, val):
        nonlocal target, answer

        if idx >= len(numbers):
            if target == val:
                answer += 1
            return
        else:
            dfs(idx+1, val+numbers[idx])
            dfs(idx+1, val-numbers[idx])

    dfs(0, 0)


    return answer

print(solution([1,1,1,1,1], 3))