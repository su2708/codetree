arr1 = [list(map(int, input().split('\n')[0].split())) for _ in range(3)]
cnt = input()
arr2 = [list(map(int, input().split('\n')[0].split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(arr1[i][j] * arr2[i][j], end=" ")
    print('')