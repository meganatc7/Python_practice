N = int(input())
paper = [[0] * 100 for _  in range(100)]

for n in range(N):

    c, r = map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[r+i][c+j] = 1

result = 0
for i in paper:
    result += sum(i)

print(result)