def searchNum(number):
    s = 0
    e = len(numbers) - 1
    while s <= e:
        mid = (s + e) // 2
        if numbers[mid] < number:
            s = mid + 1
        elif numbers[mid] > number:
            e = mid - 1
        else:
            return 1
    return 0


N = int(input())
numbers = sorted(list(map(int, input().split())))
M = int(input())
data = list(map(int, input().split()))

for num in data:
    res = searchNum(num)
    print(res)