def dfs(idx):
    for j in range(1,(idx//2)+1):
        if sel[-j:] == sel[-2*j:-j]:
            return
    if idx == N:
        return 0
    else:
        for i in range(1,4):
            sel.append(i)
            if dfs(idx+1) == 0:
                return 0
            sel.pop(-1)


N = int(input())
sel = []
dfs(0)
for i in sel:
    print(i,end='')