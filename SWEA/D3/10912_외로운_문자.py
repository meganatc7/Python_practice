T = int(input())

for t in range(1, T+1):
    words = input()
    alpha = [0] * 26

    for i in words:
        alpha[ord(i) - ord('a')] += 1
    
    result = []
    for j in range(len(alpha)):
        if alpha[j] % 2 == 1:
            result.append(chr(j+ord('a')))
    
    print('#{}'.format(t),end=' ')
    if result:
        print('{}'.format(''.join(sorted(result))))
    else:
        print('Good')