n = int(input())
count = 0

arr = [i*n for i in range(1, 11)]

for j in arr:
    if j%5 == 0:
        count += 1
        print(j, end=" ")
        if count == 2:
            break
    else:
        print(j, end=" ")