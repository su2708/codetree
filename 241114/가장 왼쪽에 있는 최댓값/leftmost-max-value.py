n = int(input())
arr = list(map(int, input().split()))

max_val = arr[0]
max_val_idx = [0]

for elem in arr[1:]:
    if elem > max_val:
        max_val = elem
        max_val_idx.append(arr.index(elem))
    
max_val_idx.reverse()
for i in max_val_idx:
    print(f"{i+1}", end=" ")