def mySort(arr): # 오름차순
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


w, h = map(int,input().split())

width = [0,w]
height = [0,h]

N = int(input())
for n in range(N):
    dire, idx = map(int,input().split())
    if dire == 1:
        width.append(idx)
    else:
        height.append(idx)

width = mySort(width)
height = mySort(height)

maxV = 0
for i in range(len(height)-1):
    for j in range(len(width)-1):
        cnt = 0
        for k in range(height[i],height[i+1]):
            for l in range(width[j],width[j+1]):
                cnt += 1
        if maxV < cnt:
            maxV = cnt
print(maxV)
