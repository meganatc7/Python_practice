while True:
    N, legs = map(int,input().split())

    if N > 1000 or legs > 4000:
        print('INPUT ERROR!')
    elif N == 0 or legs == 0:
        break
    else:
        for n in range(1,N+1):
            if n*4 + (N-n)*2 == legs:
                dog = n
                chicken = N - n
                break
        if dog and chicken:
            print(dog, chicken)
            dog, chicken = 0, 0
        else:
            print(0)