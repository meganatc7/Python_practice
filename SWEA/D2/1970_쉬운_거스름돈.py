T = int(input())

for t in range(1,T+1):
    N = int(input())//10 * 10

    change = []
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    i = 0
    for i in money:
        M, N = divmod(N, i)
        change.append(str(M))
        
    
    print(f'#{t}\n{" ".join(change)}')