n = int(input())
arr = list(map(int, input().split()))

arr.sort()
arr.reverse()

print(f"{arr[0]} {arr[1]}")