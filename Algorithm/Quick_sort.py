def partition (S, low, high):
    pivotitem = S[low]
    i = low + 1
    j = high
    while i < j:
        while i <= len(S)-1 and S[i] < pivotitem:
            i += 1
        while j >= 0 and S[j] > pivotitem:
            j -= 1
        if i < j:
            S[i], S[j] = S[j], S[i]
    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint

def quicksort(S, low, high):
    if high > low:
        pivotpoint = partition(S,low,high)
        quicksort(S, low, pivotpoint - 1)
        quicksort(S, pivotpoint + 1, high)

S = [7,5,4,1,2,10,3,6,9,8]

quicksort(S, 0, len(S) - 1)
print(S)