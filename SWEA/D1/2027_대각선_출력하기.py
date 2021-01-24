number = int(input())

for i in range(number):
    a = '#'
    b = '+'*i
    c = '+'*(number-i-1)

    print(f'{b}{a}{c}')