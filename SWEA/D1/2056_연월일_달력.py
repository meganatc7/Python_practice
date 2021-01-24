T = int(input())
count = 0

while count < T:
    now = input()
    modified_date = ''
    count += 1
    year = now[:4]
    month = now[4:6]
    date = now[6:]

    modified_date = year + '/' + month + '/' + date

    if 0< int(month) <= 12:
        if int(month) in [1,3,5,7,8,10,12]:
            if int(date) <= 31:
                print(f'#{count} {modified_date}')
            else:
                print(f'#{count} -1')
        elif int(month) in [4,6,9,11]:
            if int(date) <= 30:
                print(f'#{count} {modified_date}')
            else:
                print(f'#{count} -1')
        else:
            if int(date) <= 28:
                print(f'#{count} {modified_date}')
            else:
                print(f'#{count} -1')
    else:
        print(f'#{count} -1')

