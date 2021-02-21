# 정렬 x
arr = [4,9,11,23,19,7]

key = 2

for i in range(len(arr)):
    if arr[i] == key:
        print(i,'key가 위치한 인덱스')
        break
else:
    print('없음')

# 정렬 o
arr2 = [4,7,9,11,19,23]

key = 10

for i in range(len(arr2)):
    if key == arr2[i]:
        print(i,'key가 위치한 인덱스')
        break
    elif key < arr2[i]:
        print('없음')
        break
else:
    print('없음')