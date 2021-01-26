T = int(input())
count = 0
while count < T:
    count += 1
    t = int(input())
    total = 0
    for i in range(1, t+1):
        if i % 2:
            total += i
        else:
            total -= i
    
    print(f'#{count} {total}')
        
