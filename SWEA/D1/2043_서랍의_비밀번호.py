# 비밀번호와 예상 비밀번호 두개 값 받아오기
pw, key = map(int, input().split(' '))

# 몇번 예상해야할지 값을 저장할 변수
count = 0

# 예상 번호부터 시작해서 정답 비밀번호까지 1씩 증가하며 예측
for k in range(key,pw+1):
    # 예측 할 때마다 count에 1씩 증가
    count += 1

# 결과값 출력
print(count)