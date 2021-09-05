import sys
sys.stdin = open('data/1010.txt', 'r')

from math import factorial

cases = []
for t in range(int(input())):
    case = list(map(int, input().split()))
    cases.append(case)

for case in cases:
    N, M = case
    print(factorial(M) // (factorial(M-N) * factorial(N)))