def LPS(pat, table):
    j = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[j]:
            j += 1
            table[i] = j
            i += 1
        else:
            if j != 0:
                j = table[j-1]
            else:
                table[i] = 0
                i += 1
    return table


pat = 'ababcabcd'
table = [0] * len(pat)

print(LPS(pat,table))