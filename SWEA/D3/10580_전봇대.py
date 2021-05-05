import sys
sys.stdin = open('data/input2.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N = int(input()) # 전선의 수
    wire_group = []
    result = 0
    for n in range(N):
        wire = list(map(int, input().split())) # 현재 새로 들어온 전선

        for wg in wire_group: # 기존에 있던 전선들과 비교
            # 시작점과 끝점을 비교
            if (wire[0] < wg[0] and wire[1] > wg[1]) or (wire[0] > wg[0] and wire[1] < wg[1]):
                result += 1
        wire_group.append(wire)
    print('#{} {}'.format(t,result))