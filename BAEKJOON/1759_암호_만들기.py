def password(idx,s):
    if idx == L:
        cnt_a = 0
        cnt_b = 0
        for i in sel:
            if i in con:
                cnt_a += 1
            else:
                cnt_b += 1
        if cnt_a > 0 and cnt_b > 1:
            print(''.join(sel))
    else:
        for i in range(s,C-L+idx+1):
            sel[idx] = alpha[i]
            password(idx+1, i+1)

L,C = map(int,input().split())
alpha = sorted(list(input().split()))
con = 'aeiou'
sel = [0] * L
password(0,0)