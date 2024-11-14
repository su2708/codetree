arr = list(map(int, input().split()))

max_val, min_val = arr[0], arr[0]

for elem in arr[1:]:
    if elem == 999 or elem == -999:
        break
    elif elem > max_val:
        max_val = elem
    elif elem < min_val:
        min_val = elem
    else:
        continue

print(f"{max_val} {min_val}")