n = int(input())
arr = [1, n]

print(f"{arr[0]} {arr[1]}", end=' ')
while True:
    arr.append(arr[len(arr)-1]+arr[len(arr)-2])
    if arr[-1] > 100:
        print(arr[-1])
        break
    else:
        print(arr[-1], end=' ')