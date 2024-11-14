import itertools
n = int(input())
arr = list(map(int, input().split()))

nCr = list(itertools.combinations(arr, 2))

min_diff = 99
for elem in nCr:
    diff = elem[1]-elem[0]
    if diff < min_diff:
        min_diff = diff
    else:
        continue

print(min_diff)