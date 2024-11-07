arr = list(map(int, input().split()))
arr_even = arr[1::2]
arr_3nth = arr[2::3]

print(f"{sum(arr_even)} {round(sum(arr_3nth)/len(arr_3nth), 1)}")