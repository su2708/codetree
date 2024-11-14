n = int(input())
arr = list(map(int, input().split()))

min_val, max_val = arr[0], 100

min_dif = arr[1]-arr[0]
idx_list = [0, 1]
for idx, val in enumerate(arr[2:]):
    dif = val - min_val
    if dif-min_dif == 1:
        print(1)
        break
    elif dif-min_dif < min_dif:
        idx_list[0] = idx_list[1]
        idx_list[1] = idx
        min_val = arr[idx_list[0]]
        min_dif = dif-min_dif
    else:
        continue

print(min_dif)