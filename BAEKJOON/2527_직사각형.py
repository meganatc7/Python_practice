T = 4
for t in range(1,T+1):
    lst = list(map(int,input().split())
    X, Y, P, Q = lst[0], lst[1], lst[2], lst[3]
    x, y, p, q = lst[4], lst[5], lst[6], lst[7]

    if x < P and y < Q and p > X and q > Y:
        result = 'a'

    elif (x < P and y == Q and p > X) or (y < Q and p == X and q > Y) or (x < P and q == Y and p > X) or (y < Q and x == P and q > Y):
        result = 'b'
    
    elif X == p and Y == q or X == p and Q == y or P == x and Q == y or P == x and Y == q:
        result = 'c'

    else:
        result='d'

    print(result)
