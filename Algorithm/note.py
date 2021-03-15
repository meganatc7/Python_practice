def comb(idx,s):
    if idx == R:
        print(sel)
    else:
        for i in range(s,N-R+1+idx):
            sel[idx] = i
            comb(idx+1,i+1)


N = 5
R = 3
sel = [-1] * R
comb(0,0)