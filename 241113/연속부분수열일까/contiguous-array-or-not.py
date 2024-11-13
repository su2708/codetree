n1, n2 = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

start = arr_b[0]

len_a =len(arr_a)
len_b = len(arr_b)
arr_b.sort()

for i in range(len_a):
    if start not in arr_a:
        print('No')
        break
    elif len(arr_a[i:]) < len_b:
        print('No')
        break
    else:
        arr = arr_a[i:i+len_b]
        arr.sort()
        if arr == arr_b:
            print('Yes')
            break
        else:
            arr_a = arr_a[i+1:]
            continue