import sys
sys.stdin = open('data/sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    pat = input()
    word = input()
    ans = 0
    for i in range(len(word) - len(pat)+1):
        if pat == word[i:i+len(pat)]:
            ans = 1
            break
    print('#{} {}'.format(t,ans))