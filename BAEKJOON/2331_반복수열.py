A, P = map(int,input().split())

lst = [A]
#chk = [0] * 300000
while True:
    a = 0
    for num in str(lst[-1]):
        a += (int(num)**P)
    if a not in lst:
        lst.append(a)
    else:
        break
cnt = 0
for num in lst:
    if num == a:
        break
    cnt += 1

print(cnt)