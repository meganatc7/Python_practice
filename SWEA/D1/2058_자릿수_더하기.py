T = int(input())
total = 0
while T / 10:
    remainder = T % 10
    T = T // 10
    total += remainder
print(total)
