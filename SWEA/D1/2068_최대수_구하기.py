T = int(input())
count = 0

while count < T:
    max = 0
    total = 0
    num_list = list(map(int,input().split(' ')))
    for i in num_list:
        if i > max:
            max = i
    count += 1
    print(f'#{count} {max}')
        