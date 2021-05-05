def func(p,n):
    tmp = numbers
    left = True
    bool = [True, False]
    k = 0
    for i in p:
        if i == 'R':
            left = bool[(k+1)%2]
            k += 1
        else:
            if left:
                tmp.pop(0)
            else:
                tmp.pop(-1)
    if left:
        return tmp
    else:
        return tmp[::-1]

T = int(input())
for t in range(T):
    P = input()
    N = int(input())
    tmp = input()
    if N != 0 and N >= P.count('D'):
        numbers = list(map(int, tmp[1:-1].split(',')))
        print(str(func(P, N)).replace(' ',''))
    else:
        print('error')