def computeLPS(pat,lps):
    j = 0
    i = 1

    while i < len(pat):
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if  j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1

def KMPsearch(txt,pat):
    N = len(txt)
    M = len(pat)
    lps = [0] * M
    computeLPS(pat,lps)

    i = 0
    j = 0

    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        
        if j == M:
            print('패턴발견',str(i-j))
            j = lps[j-1]



txt = 'aabaabccabcbaabbccabcaxcvabaabccabcxcaabaabccabczxcabaabccabc'
pat = 'abaabccabc'
KMPsearch(txt,pat)