nineDwarfs = []
for i in range(9):
    nineDwarfs.append(int(input()))

for i in range(1<<9):
    Dwarfs = []
    for j in range(9):
        if i & (1<<j):
            Dwarfs.append(nineDwarfs[j])
    if len(Dwarfs) == 7 and sum(Dwarfs) == 100:
        break

for i in sorted(Dwarfs):
    print(i)