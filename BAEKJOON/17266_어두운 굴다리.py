# 굴다리 길이
N = int(input())
# 가로등 수
M = int(input())
lights = list(map(int,input().split())) # 가로등의 위치

if len(lights) == 1:
    height = max(lights[0], N - lights[0])
else:
    height = lights[0]
    for i in range(len(lights)):
        if i == (len(lights) - 1):
            tmp = N - lights[-1]
        else:
            a = lights[i+1] - lights[i]
            if a % 2:
                tmp = a // 2 + 1
            else:
                tmp = a // 2

        height = max(height, tmp)


print(height)