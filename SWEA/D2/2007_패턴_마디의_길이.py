T = int(input())
count = 0
while count < T:
    count += 1
    problem = input()
    pattern = []
    for i in range(1,11):
        pattern.append(problem[:i])
    
    for i in range(10):
        tmp = len(pattern[i])
        if problem[:tmp] == problem[tmp:tmp+tmp]:
            print(f'#{count} {tmp}')
            break
    