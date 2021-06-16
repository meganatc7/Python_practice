import sys
sys.stdin = open('data/sample_input4.txt', 'r')

def cal(data):
    st = []
    for d in data:
        if d.isdigit():
            st.append(d)
        elif d == '.':
            if len(st) > 1:
                return 'error'
            return st[0]
        else:
            try:
                b = int(st.pop(-1))
                a = int(st.pop(-1))
                if d == '+':
                    res = a + b
                elif d == '-':
                    res = a - b
                elif d == '*':
                    res = a * b
                elif d == '/':
                    res = a // b
                st.append(res)
            except:
                return 'error'
    return 'error'



T = int(input())
for t in range(1, T+1):
    data = input().split()
    ans = ''
    if data[0].isdigit() and data[1].isdigit():
        ans = cal(data)
    else:
        ans = 'error'

    print('#{} {}'.format(t,ans))