# 재귀를 활용한 순열 (제일 이해하기 무난!! 이거랑 추가적으로 bit까지만 이해해보기)
def perm(idx):
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if chk[i] == 0:
                sel[idx] = arr[i]
                chk[i] = 1
                perm(idx+1)
                chk[i] = 0

arr = [1,2,3]
N = len(arr)

sel = [0] * N
chk = [0] * N
perm(0)
