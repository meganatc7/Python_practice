import sys
import heapq

N = int(input())
heap = []
for n in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, tmp)
