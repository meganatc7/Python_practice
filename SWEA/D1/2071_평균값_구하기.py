T = int(input())
count = 0

while count < T:
    total = 0
    num_list = list(map(int,input().split(' ')))
    for i in num_list:
        total += i
    avg = round(total / len(num_list))
    count += 1
    print(f'#{count} {avg}')
        