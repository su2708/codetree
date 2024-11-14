n = int(input())
arr = list(map(int, input().split()))

min_val = arr[0]
cnt = 1

for elem in arr:
    if elem == min_val:
        cnt += 1
    elif elem < min_val:
        min_val = elem
        cnt = 1
    else:
        continue

print(f"{min_val} {cnt}")