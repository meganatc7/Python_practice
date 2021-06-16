import sys
sys.stdin = open('data/sample_input3.txt', 'r')

T = int(input())

for t in range(1,T+1):
    str1 = input()
    str2 = input()
    dict = {}

    for i in range(len(str1)):
        for j in range(i,len(str1)):
            tmp = str1[i:j+1]
            dict[tmp] = 0
    for key in dict:
        dict[key] = str2.count(key)

    maxV = 0
    res = ''
    for key, value in dict.items():
        if maxV < value:
            maxV = value
            res = key

    print('#{} {}'.format(t,maxV))