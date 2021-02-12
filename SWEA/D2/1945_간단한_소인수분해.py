T = int(input())

for t in range(1,T+1):
    N = int(input())

    num = [2, 3, 5, 7, 11]

    result = []
    for i in num:
        cnt = 0
        while N % i == 0:
            N //= i
            cnt += 1
        result.append(cnt)

    print('#{} {}'.format(t, ' '.join(map(str,result))))
