from pprint import pprint

brd = [[0]*100 for _ in range(100)]
for t in range(4):
    a, b, c, d = map(int,input().split())

    for i in range(b,d):
        for j in range(a,c):
            brd[i][j] = 1
            
total = 0
for i in brd:
    for j in i:
        total += j
print(total)