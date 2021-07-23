import sys
sys.stdin = open('data/input12.txt', 'r')

import itertools

T = int(input())
for t in range(1,T+1):
    numbers = list(map(int, input().split()))
    perm = list(itertools.permutations(numbers,3))

    sum_lst = []
    for i in range(len(perm)):
        tmp = sum(perm[i])
        sum_lst.append(tmp)
    sum_lst = list(set(sum_lst))

    sum_lst.sort(reverse=True)
    print('#{} {}'.format(t,sum_lst[4]))