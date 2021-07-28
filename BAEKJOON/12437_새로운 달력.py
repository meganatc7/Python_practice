T = int(input())
for t in range(T):
    totalMonth, totalDayOfMonth, totalDayOfWeek = map(int, input().split())
    calendar = 0
    for i in range(totalMonth):
        a, b = divmod(totalDayOfMonth, totalDayOfWeek)
        if b:
            calendar += a + 1
            if i != totalMonth -1 :
                calendar += 1
        else:
            calendar += a

    print(calendar)

