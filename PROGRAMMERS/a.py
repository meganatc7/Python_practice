from itertools import product

l = [(1,-1),(2,-2),(3,-3)]

s = list(product(*l))

print(s)