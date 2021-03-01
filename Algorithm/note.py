def LPS(pat,lps):
    i, j = 1, 0

    while i < len(pat):
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = j
                i += 1

def KMP(pat,txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    LPS(pat,lps)
    cnt = 0

    i, j = 0, 0

    while i < N:
        if pat[j] == txt[i]:
            j += 1
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == M:
            print('패턴발견'+str(i-j))
            cnt += 1
            j = lps[j-1]
    print(cnt)


txt = 'ABXABABXAB'
pat = 'ABXAB'

KMP(pat,txt)