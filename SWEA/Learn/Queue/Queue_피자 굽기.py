import sys
sys.stdin = open('data/data1.txt', 'r')

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    pizzas = []
    for m in range(M):
        pizzas.append([tmp[m],m+1])

    oven = [0] * N
    for n in range(N):
        pizza = pizzas.pop(0)
        oven[n] = pizza

    idx = 0
    while oven:
        p = oven.pop(0)
        if p[0] != 0:
            p[0] //= 2
            oven.append(p)
        else:
            if pizzas:
                pizza = pizzas.pop(0)
                pizza[0] //= 2
                oven.append(pizza)

    print('#{} {}'.format(t,p[1]))