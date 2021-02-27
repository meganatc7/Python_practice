def i_is_wall(i):
    global a
    if i == u_wall or i == d_wall:
        a += 1
        a %= 2

def j_is_wall(j):
    global b
    if j == l_wall or j == r_wall:
        b += 1
        b %= 2

d = [1, -1]
a = 0
b = 0
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
l_wall = 0
r_wall = w
u_wall = h
d_wall = 0
i = q
j = p
i_t = t % (2 * h)
j_t = t % (2 * w)

k = 0
while True:
    if k == j_t:
        print(j, end=" ")
        break
    j_is_wall(j)
    j += d[b]
    k += 1

k = 0
while True:
    if k == i_t:
        print(i)
        break
    i_is_wall(i)
    i += d[a]
    k += 1