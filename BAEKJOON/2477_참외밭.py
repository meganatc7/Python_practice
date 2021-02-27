N = int(input())

field = [list(map(int,input().split())) for _ in range(6)]*2

# 작은 사각형
for i in range(len(field)-4+1):
    tmp = field[i:i+4]
    if tmp[0][0] == tmp[2][0] and tmp[1][0] == tmp[3][0]:
        small_square = (tmp[1][1] * tmp[2][1])
        break
        
# 큰 사각형
length_w = []
length_h = []
for i in field:
    if i[0] == 3 or i[0] == 4:
        length_h.append(i[1])
    else:
        length_w.append(i[1])
height = max(length_h)
width = max(length_w)
big_square = height * width

result = big_square - small_square
print(result*N)

