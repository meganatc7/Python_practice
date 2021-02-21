arr = [1,3,5,1,6,7,10,23]

key = 10

start = 0
end = len(arr)-1

while start <= end:
    middle = (start + end) // 2
    if key == arr[middle]:
        print(middle,'key의 위치 인덱스')
    elif arr[middle] > key:
        end = middle - 1
    else:
        start = middle + 1