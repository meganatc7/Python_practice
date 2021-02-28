arr = [1,2,3]
N = len(arr)

sel = [0] * N
chk = [0] * N

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

#perm(0)

# 비트를 활용한 순열(아지은 어색)
def perm_bit(idx,check):
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            # i번째 원소를 활용했다면 사용하지 않도록 컨티뉴
            if check & (1<<i): continue

            sel[idx] = arr[i]
            perm_bit(idx+1, check | (1<<i)) # 원상복구 과정이 필요가 없음
        
#perm_bit(0,0)

# 스왑을 활용한 순열 (이것두 좀...)
def perm_swap(idx):
    if idx == N:
        print(arr)
    else:
        for i in range(N):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm_swap(idx+1)
            arr[idx], arr[i] = arr[i], arr[idx]

perm_swap(0)