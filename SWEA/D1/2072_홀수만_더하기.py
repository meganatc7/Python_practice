T = int(input())
count = 0

while count < T:
    sum = 0
    num_list = list(map(int,input().split(' ')))
    for i in num_list:
        if i % 2:
            sum += i
    count += 1
    print(f'#{count} {sum}')