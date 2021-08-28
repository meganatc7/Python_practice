import heapq
import sys

N = int(input())
heap = []
res = []
tmp = []
for n in range(N):
    num = int(sys.stdin.readline())
    tmp.append(num)

for num in tmp:
    if num == 0:
        if len(heap) > 0:
            max_num = heapq.heappop(heap)
            res.append(max_num * -1)
        else:
            res.append(0)
    else:
        heapq.heappush(heap, num * -1)

for i in res:
    print(i)