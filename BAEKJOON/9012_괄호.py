T = int(input())
for t in range(T):
    brackets = input()
    st = []
    flag = False
    for bracket in brackets:
        if bracket == "(":
            st.append(bracket)
        elif bracket == ")":
            if len(st) == 0:
                flag = True
                print('NO')
                break
            else:
                st.pop()
    if not flag:
        if len(st) > 0:
            print('NO')
        else:
            print('YES')