num_s = int(input())
switch = list(map(int,input().split()))
num_p = int(input())
for n in range(num_p):
    sex, num = map(int,input().split())

    if sex == 1:
        i = 1
        while num * i - 1 < len(switch):
            if switch[num * i - 1]:
                switch[num * i - 1] = 0
            else:
                switch[num * i - 1] = 1
            i += 1
    
    else:
        j = 0
        while (num - 1 - j) >= 0 and (num - 1 + j) < len(switch) and switch[num -1 - j] == switch[num -1 + j]: 
            if j == 0:
                for k in range(num - 1 - j , num - 1 + j + 1):
                    if switch[k]:
                        switch[k] = 0
                    else:
                        switch[k] = 1
            else:
                for k in range(num - 1 - j , num - 1 + j + 1, j * 2):
                    if switch[k]:
                        switch[k] = 0
                    else:
                        switch[k] = 1
            j += 1
                

result = []
for i in switch:
    result.append(str(i))

for j in range(1,len(result)//20+2):
    print(' '.join(result[20*(j-1):20*j]))