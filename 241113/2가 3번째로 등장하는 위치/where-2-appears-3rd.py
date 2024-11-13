n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for idx, i in enumerate(arr):
    if i==2:
        cnt += 1
        if cnt==3:
            print(idx+1)