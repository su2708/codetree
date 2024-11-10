arr = list(map(int, input().split()))

sum_odd, sum_even = 0, 0

for i in range(len(arr)):
    if i%2 == 0:
        sum_odd += arr[i]
    else:
        sum_even += arr[i]

result = sum_even - sum_odd
if result<0:
    result = result*(-1)

print(result)