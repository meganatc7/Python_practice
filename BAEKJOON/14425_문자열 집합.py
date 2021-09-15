N, M = map(int ,input().split())
word_group = {}
for n in range(N):
    word = input()
    word_group[word] = 1
res = 0
for m in range(M):
    chk_word = input()
    if word_group.get(chk_word):
        res += 1

print(res)
