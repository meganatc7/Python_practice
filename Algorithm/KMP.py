def computeLPS(pat, lps):
    leng = 0

    # 항상 lps[0]은 0이므로 while문은 i==1부터 시작
    i = 1
    while i < len(pat):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 됨
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else: # 일치하지 않는 경우
            if leng != 0:
                # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
                # 접두사와 접미사를 맞춰주기 위해 점프!!
                leng = lps[leng-1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0이고 i는 1 증가
                lps[i] = 0
                i += 1


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0] * M
    # 패턴 테이플 생성해주고~
    computeLPS(pat,lps)
    
    i = 0 # txt의 인덱스
    j = 0 # pat의 인덱스
    while i < N: # i는 그냥 성큼성큼 하나씩 계속 N미만 까지 증가
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
        if pat[j] == txt[i]:
            i += 1
            j += 1
        #1 같지 않은 경우, 즉 패턴을 찾지 못한경우
        elif pat[j] != txt[i]:
            # j != 0 인경우는 짧은 lps에 대해 재검사
            if j != 0:
                j = lps[j-1]
            # j = 0이면 일치하는 부분이 없으므로 인덱스 증가
            else:
                i += 1
        #2 패턴을 찾은 경우
        if j == M:
            print("패턴 발견" + str(i-j))
            # 이전 인덱스의 lps값을 참조하여 계속 검색
            j = lps[j-1]

txt = 'ABXABABXAB'
pat = 'ABXAB'

KMPSearch(pat,txt)