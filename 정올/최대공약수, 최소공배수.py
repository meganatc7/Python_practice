def UC(X, Y):
    while Y:
        X, Y = Y, X % Y
    return X

def LCM(X, Y):
    if X < Y:
        max = Y
    else:
        max = X

    for i in range(max, (X*Y)+1):
        if i % X == 0 and i % Y == 0:
            res = i
            break
    return res

N = int(input())
nums = sorted(list(map(int,input().split())))

uc = UC(nums[0], nums[1])
lcm = LCM(nums[0], nums[1])

for n in range(2,N):
    uc = UC(uc,nums[n])
    lcm = LCM(lcm,nums[n])

print(uc, lcm)

