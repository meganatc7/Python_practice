T = input()
count = 0

if len(T) == 8:
    while count < T:
        now = input()
        count += 1
        year = now[:4]
        month = now[4:6]
        date = now[6:]


