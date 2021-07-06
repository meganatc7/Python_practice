N = int(input())
vote = int(input())
students_num = list(map(int, input().split()))

photos = []
tmp = []

for i in range(vote):
    if students_num[i] in photos:
        for j in range(len(photos)):
            if students_num[i] == photos[j]:
                tmp[j] += 1
    else:
        if len(photos) >= N:
            for j in range(N):
                if tmp[j] == min(tmp):
                    del photos[j]
                    del tmp[j]
                    break
        photos.append(students_num[i])
        tmp.append(1)

photos.sort()
print(' '.join(map(str,photos)))
