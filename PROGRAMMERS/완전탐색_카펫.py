def solution(brown, yellow):
    answer = []

    tmp_brown = (brown - 4) // 2
    w = 0
    h = 0
    for i in range(tmp_brown):
        if i * (tmp_brown - i) == yellow:
            h = i
            w = tmp_brown - i

    answer.append(h + 2)
    answer.append(w + 2)
    return answer

solution(10,2)