arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] != 0:
        continue
    else:
        result = sum(arr[i-3:i])
        print(result)
        break