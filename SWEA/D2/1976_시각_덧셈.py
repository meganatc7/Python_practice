T = int(input())

for t in range(1,T+1):
    time = list(map(int,input().split()))

    hour_1 = time[0]
    hour_2 = time[2]
    minute_1 = time[1]
    minute_2 = time[3]

    result_hour = 0
    result_minute = 0

    exceeded_minute, result_minute = divmod(minute_1 + minute_2, 60)
    result_hour = exceeded_minute + hour_1 + hour_2
    if result_hour > 12:
        result_hour = result_hour - 12

    print(f'#{t} {result_hour} {result_minute}')


