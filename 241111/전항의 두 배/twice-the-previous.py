arr = list(map(int, input().split()))
print(f"{arr[0]} {arr[1]}", end=' ')

while True:
    arr.append(arr[len(arr)-1] + 2*arr[len(arr)-2])
    if len(arr) < 10:
        print(arr[-1], end=' ')
    else:
        print(arr[-1])
        break