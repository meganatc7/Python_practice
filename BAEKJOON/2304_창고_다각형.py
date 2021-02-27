def getMax():
    maxV = 0
    for c in col:
        if c[1] > maxV:
            maxV = c[1]
            maxidx = c[0]
    return maxV, maxidx

def mySort():
    for i in range(len(col)-1):
        for j in range(i,len(col)):
            if col[i][0] > col[j][0]:
                col[i], col[j] = col[j], col[i]

N = int(input())

col = [list(map(int,input().split())) for _ in range(N)]
mySort()
maxH, maxidx = getMax()
leng = col[N-1][0] + 1 # 공장 0부터 기둥까지 가로길이
total = 0

# 앞에서 가장 높은 기둥까지
j = 0
tmp = 0
for i in range(maxidx+1):
    if i == col[j][0]:
        if tmp < col[j][1]:
            tmp = col[j][1]
        j += 1
    total += tmp

    
# 뒤에서 가장 높은 기둥까지
k = N - 1
tmp = 0
for i in range(leng-1,maxidx,-1):
    if i == col[k][0]:
        if tmp < col[k][1]:
            tmp = col[k][1]
        k -= 1
    total += tmp

print(total)