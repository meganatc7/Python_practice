T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = sorted(list(map(int,input().split())))

    res = nums[-1] - nums[0]

    print('#{} {}'.format(t, res))