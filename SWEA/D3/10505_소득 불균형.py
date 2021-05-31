import sys
sys.stdin = open('data/input3.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    incomes = list(map(int,input().split()))

    avg_income = sum(incomes) / len(incomes)

    cnt= 0
    for income in incomes:
        if income <= avg_income:
            cnt += 1

    print('#{} {}'.format(t,cnt))