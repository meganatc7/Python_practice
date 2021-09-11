import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while True:

        if scoville[0] >= K:
            break
        if len(scoville) < 2:
            answer = -1
            break
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        num = a + (b * 2)
        heapq.heappush(scoville, num)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))



# a = [5,3,2,1,7]
# heapq.heapify(a)
# b = heapq.heappop(a)
# print(b)