import sys
sys.stdin = open('data/sample_input6.txt', 'r')

def game(i, j):
    if i == j:
        return i
    a = game(i,(i+j)//2)
    b = game((i+j)//2+1,j)

    if cards[a] == 1:
        if cards[b] == 1:
            return a
        elif cards[b] == 2:
            return b
        elif cards[b] == 3:
            return a
    if cards[a] == 2:
        if cards[b] == 1:
            return a
        elif cards[b] == 2:
            return a
        elif cards[b] == 3:
            return b
    if cards[a] == 3:
        if cards[b] == 1:
            return b
        elif cards[b] == 2:
            return a
        elif cards[b] == 3:
            return a




T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    print('#{} {}'.format(t,game(0,N-1)+1))