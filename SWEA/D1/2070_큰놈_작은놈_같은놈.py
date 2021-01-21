T = int(input())
count = 0

while count < T:
    count += 1
    a, b = map(int, input().split(' '))
    if a < b:
        print(f'#{count} <')
    elif a == b:
        print(f'#{count} =')
    else:
        print(f'#{count} >')

