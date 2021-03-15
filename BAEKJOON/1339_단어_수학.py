N = int(input())
word = []
for n in range(N):
    tmp = []
    for i in input():
        tmp.append(ord(i) - 65)
    word.append(tmp)

chk = [0] * 26

for i in range(N):
    j = 0
    for k in word[i][::-1]:
        chk[k] += (10 ** j)
        j += 1

chk.sort(reverse=True)

ans = 0
t = 9
for i in range(26):
    if chk[i] == 0: break
    ans += (chk[i] * t)
    t -= 1

print(ans)

