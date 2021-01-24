T = int(input())
count = 0

while count < T:
    count += 1
    number, div = map(int,input().split(' '))
    share = number // div
    rest = number % div
    print(f'#{count} {share} {rest}')