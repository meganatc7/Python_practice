T = int(input())

for t in range(1,T+1):
    num = int(input())
    print(f'#{t}')
    pascal_1 = [1]
    pascal_2 = []
    for i in range(1, num+1):
        # 첫줄인 경우 본래 리스트에 담아뒀던 1을 출력
        if i == 1:
            print(' '.join(list(map(str,pascal_1))))
        # 두번째 줄인 경우 1 1 이니까 리스트에 1을 하나 추가헤서 출력
        elif i == 2:
            pascal_1.append(1)
            print(' '.join(list(map(str,pascal_1))))
            pascal_2 = pascal_1[:]
        # 두번째 줄 이후에는
        else:
            for j in range(i):
                # 리스트의 첫번째 인덱스(0)은 무조건 1
                if j == 0:
                    pascal_1[j] = 1
                # 리스트의 마지막 번째 인덱스는 무조건 1이니까 마지막 차례때는 1을 append
                elif j == i-1:
                    pascal_1.append(1)
                # 나머지 리스트 요소에는 이전의 리스트(pascal_2)의 현재 인덱스 -1과 현재 인덱스를 더한 값
                else:
                    pascal_1[j] = pascal_2[j-1] + pascal_2[j]
            # 결과적인 리스트 출력        
            print(' '.join(list(map(str,pascal_1))))
            # 다음 연산때 쓰기 위해 pascal_2에 리스트를 저장
            pascal_2 = pascal_1[:]
