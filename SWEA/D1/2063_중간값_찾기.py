T = int(input())
num_list = list(map(int, input().split(' ')))
if T == len(num_list):
    num_list.sort()
    middle = T // 2
    print(num_list[middle])
else:
    raise Exception('개수를 초과했습니다.')
