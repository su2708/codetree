total = 0
for i in range(4):
    arr = list(map(int, input().split()))
    if i < 3:
        result = sum(arr) - sum(arr[i+1:])
        total += result
    else:
        total += sum(arr)

print(total)