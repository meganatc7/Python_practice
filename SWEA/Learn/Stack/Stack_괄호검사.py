import sys
sys.stdin = open('data/sample_input.txt', 'r')

def f(data):
    st = []
    for w in data:
        if w == '(' or w == '{':
            st.append(w)
        elif w == ')' or w == '}':
            if len(st) == 0:
                return 0
            elif (w == '}' and st[-1] == '{') or (w == ')' and st[-1] == '('):
                st.pop(-1)
            else:
                return 0
    if st:
        return 0
    else:
        return 1

T = int(input())
for t in range(1,T+1):
    data = input()
    ans = f(data)

    print('#{} {}'.format(t,ans))

