T = int(input())

for t in range(1,T+1):
    A, B = map(int,input().split())
    cnt = 0
    for i in range(A,B+1):
        tmp = i ** (1/2)
        if i == tmp ** 2:
            sqrt = str(tmp)[:-2]
            #print(sqrt,i)
            if str(i) == str(i)[::-1] and sqrt == sqrt[::-1]:
                cnt += 1

    print('#{} {}'.format(t,cnt))
