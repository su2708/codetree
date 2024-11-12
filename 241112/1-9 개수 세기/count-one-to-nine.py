n = int(input())
arr = list(map(int, input().split()))
cnt_arr = [0 for _ in range(9)]

for i in arr:
    cnt_arr[i-1] += 1

for j in cnt_arr:
    print(j)