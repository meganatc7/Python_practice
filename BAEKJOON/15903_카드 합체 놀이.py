import heapq

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
heapq.heapify(numbers)

for _ in range(m):
    a = heapq.heappop(numbers)
    b = heapq.heappop(numbers)
    c = a + b
    heapq.heappush(numbers, c)
    heapq.heappush(numbers, c)

print(sum(numbers))