n = int(input())
arr = list(map(int, input().split()))

min_val, max_val = arr[0], arr[0]

for elem in arr[1:]:
    if min_val > elem:
        min_val, max_val = elem, elem
    
    if max_val < elem:
        max_val = elem

print(max_val - min_val)    