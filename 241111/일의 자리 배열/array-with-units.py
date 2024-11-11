arr = list(map(int, input().split()))

for i in range(2, 10):
    result = arr[i-1] + arr[i-2]
    if result>9:
        result = result-10
    arr.append(result)

for i in range(len(arr)):
    print(arr[i], end=" ")