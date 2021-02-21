T = int(input())

for t in range(1,T+1):
    word = input()

    ans = ''
    for i in word[::-1]:
        if i == 'd':
            ans += 'b'
        elif i == 'b':
            ans += 'd'
        elif i == 'q':
            ans += 'p'
        elif i == 'p':
            ans += 'q'

    print('#{} {}'.format(t,ans))