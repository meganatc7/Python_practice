import sys
sys.stdin = open('data/input10.txt', 'r')

TC = int(input())

for t in range(1, TC+1):
    pattern = input()
    res = [1,1]
    for pat in pattern:
        a = res[0]
        b = res[1]
        if pat == 'L':
            res[0] = a
            res[1] = a + b
        elif pat == 'R':
            res[0] = a + b
            res[1] = b
    print("#{} {} {}".format(t, res[0], res[1]))
