m, n = map(int, input().split())

cnt = 1
for i in range(m):
    for j in range(n):
        print(cnt, end=" ")
        cnt += 1
    print('')