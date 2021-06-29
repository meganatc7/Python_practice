while True:
    try:
        a, b, c, d, m, t = map(float, input().split())
        s = 0
        e = 10 ** 10
        cnt = 0

        while s <= e:
            if cnt > 800:
                break
            mid = (s + e) / 2
            oil = (a*(mid**4) + b*(mid**3) + c*(mid**2) + d*mid) * (m / mid)
            if oil <= t:
                s = mid
            else:
                e = mid
            cnt += 1

        print(int(e*100)/100)
    except: break