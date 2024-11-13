n1, n2 = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

indice = [idx for idx, val in enumerate(arr_a) if val==arr_b[0]]

length = len(arr_b)
arr_b.sort()
cnt = len(indice)

for idx in indice:
    cnt -= 1
    if len(arr_a[idx:]) < length:
        print('No')
        break
    else:
        arr = arr_a[idx:idx+length]
        arr.sort()
        if arr == arr_b:
            print('Yes')
            break
        else:
            if cnt!=0:
                continue
            else:
                print('No')
                break