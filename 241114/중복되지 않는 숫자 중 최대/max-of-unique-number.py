n = int(input())
arr = list(map(int, input().split()))

arr.sort()
arr_set = list(set(arr))

for i in range(len(arr_set)-1, -1, -1):
    max_val = arr_set[i]
    if arr.count(max_val) == 1:
        print(max_val)
        break
    
    if i == 0:
        print(-1)
        