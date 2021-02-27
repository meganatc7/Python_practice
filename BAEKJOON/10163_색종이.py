paper = [[0] * 101 for _ in range(101)]

N = int(input())
for n in range(1,N+1):
    a, b, w, h = input().split()
    r = 100 - int(b)
    c = int(a)
    w = int(w)
    h = int(h)
    for i in range(r-h+1,r+1):
        for j in range(c,c+w):
            paper[i][j] = n

for n in range(1,N+1):
    cnt = 0
    for i in range(len(paper)):
        for j in range(len(paper)):
            if paper[i][j] == n:
                cnt += 1
    print(cnt)
