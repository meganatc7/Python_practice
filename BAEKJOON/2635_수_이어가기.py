st = int(input())

max_length = 0

for i in range(st,-1,-1):
    tmp = [st]
    tmp.append(i)
    j = 0
    while tmp[j] - tmp[j+1] >= 0:
        tmp.append(tmp[j]-tmp[j+1])
        j += 1

    if max_length < len(tmp):
        max_length = len(tmp)
        result = tmp

print(max_length)
for i in result:
    print(i, end=' ')