# 비트연산으로 부분집합 구하기
arr = [1,2,3]

n = len(arr)
                        # 결국 그 인덱스의 요소가 있느냐 없느냐가 중요
for i in range(1<<n): # 2진수로 나타낸 부분집합 경우의 수(1<<n = 2^n)
    for j in range(n): # j의 인덱스값을 순회
        if i & (1<<j):  # 해당 경우에 j의 인덱스가 들어있다면 
            print(arr[j],end=',')
    print()


# powerset 부분집합 구하기
def powerset(idx):
    if idx == N:
        print(sel)
    else:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)


arr_1 = [1,2,3,4]
N = len(arr_1)
sel = [0] * N
powerset(0)
# >> arr_1의 0번 인덱스 부터 시작해서 재귀함수를 통해 부분집합을 구하는 것
# 0번, 1번, 2번, 3번 (뽑는게 18번라인, 안뽑는게 20번라인)
# 뽑고 뽑고 뽑고 (뽑고,안뽑고) 2
# 뽑고 뽑고 안뽑고 (뽑고,안뽑고) 2
# 뽑고 안뽑고 뽑고 (뽑고,안뽑고) 2
# 뽑고 안뽑고 안뽑고 (뽑고,안뽑고) 2 여기까지 8가지 경우
# 안뽑고로 시작해서 또 8가지 경우
# 따라서 2의 4승의 부분집합 가지의 수 16개 완성!
