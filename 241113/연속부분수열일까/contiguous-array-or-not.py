n1, n2 = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

indice = [idx for idx, val in enumerate(arr_a) if val==arr_b[0]]

for idx in indice:
    if len(arr_a[idx:]) < len(arr_b):
        print('No')
        break
    else:
        arr = arr_a[idx:len(arr_b)+idx]
        arr.sort()
        arr_b.sort()
        if arr == arr_b:
            print('Yes')
            break
        else:
            continue