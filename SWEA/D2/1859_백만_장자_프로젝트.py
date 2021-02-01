T = int(input())

count = 0

while count < T:
    count += 1
    day = int(input())
    # 물건들의 가격을 쭉 나열해서 리스트로
    price = list(map(int, input().split()))
    # 맨 마지막 날의 가격을 last변수에 저장
    last = price[-1]
    # 이윤을 나타낼 변수 선언
    benefit = 0
    # 뒤에서 부터 순회
    for i in range(len(price)-1, -1, -1):
        # 만약 뒤에서 순회하는 값보다 last값이 크면
        if last > price[i]:
            # 이윤에 싼거 사고 비싼거 팔고
            benefit += last - price[i]
        # 만약 last값보다 순회한 값이 더 크거나 같다면
        else:
            # last에 그 큰 값을 저장
            last = price[i]
    print(f'#{count} {benefit}')