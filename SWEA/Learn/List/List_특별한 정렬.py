import sys
sys.stdin = open('data/sample_input8.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    numbers = sorted(list(map(int,input().split())))
    lst = []
    for i in range(10):
        if i % 2:
            lst.append(numbers.pop(0))
        else:
            lst.append(numbers.pop(-1))

    print('#{} {}'.format(t,' '.join(map(str,lst))))