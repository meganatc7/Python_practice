# def divisor(num):
#     lst = []
#     while num > 0:
#         lst.append(num)
#         num //= 2
#     return sorted(lst)

def doublemaker(data):
    for i in range(1,data+1):
        tmp = data * i
        sqrt = int(tmp ** (0.5))
        if tmp == sqrt ** 2:
            return i

            
T = int(input())

for t in range(1,T+1):
    A = int(input())
    ans = doublemaker(A)

    print('#{} {}'.format(t,ans))

