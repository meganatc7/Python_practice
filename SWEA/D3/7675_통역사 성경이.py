import sys
sys.stdin = open('data/input7.txt', 'r')

for t in range(1, int(input())+1):
    N = int(input())
    pharagraph = list(input().strip().replace('?','.').replace('!','.').split('.'))
    res = []
    for sentence in pharagraph:
        if sentence:
            tmp = sentence.split()
            cnt = 0
            for word in tmp:
                if word[0].isupper():
                    if not any(letter.isdigit() for letter in word) and not any(letter.isupper() for letter in word[1:]):
                        cnt += 1
            res.append(cnt)
    print('#{} {}'.format(t, ' '.join(map(str, res))))


