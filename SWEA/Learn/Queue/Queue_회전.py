import sys
sys.stdin = open('data/sample_input1.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    nums = list(map(int, input().split()))
    print('#{} {}'.format(t,nums[M%N]))



