import sys
sys.stdin = open('data/sample_input3.txt', 'r')

T = int(input())
for t in range(1,T+1):
    data = input()
    st = []

    for d in range(len(data)):
        if len(st) == 0:
            st.append(data[d])
        else:
            if st[-1] == data[d]:
                st.pop(-1)
            else:
                st.append(data[d])

    print('#{} {}'.format(t,len(st)))
