import sys
sys.stdin = open('data/input9.txt', 'r')

TC = int(input())

for t in range(1,TC+1):
    N = int(input())

    # 약수 배열
    lst = []

    for n in range(1, N+1):
        if N % n == 0:
            lst.append(n)

    res = 'No'
    idx = 0
    if len(lst) % 2:
        while idx < len(lst)//2 + 1:
            if lst[idx] <= 9 and lst[len(lst)-1-idx] <= 9:
                res = 'Yes'
                break
            idx += 1
    else:
        while idx < len(lst)//2:
            if lst[idx] <= 9 and lst[len(lst)-1-idx] <= 9:
                res = 'Yes'
                break
            idx += 1
    print('#{} {}'.format(t, res))