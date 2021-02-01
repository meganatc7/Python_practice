T = int(input())

for t in range(1,T+1):
    num = int(input())
    print(f'#{t}')
    pascal_1 = [1]
    pascal_2 = [1]
    for i in range(1, num+1):
        for number in pascal_2:
            print(number, end=' ')
        pascal_2.append
