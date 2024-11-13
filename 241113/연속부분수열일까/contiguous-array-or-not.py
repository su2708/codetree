n1, n2 = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

if arr_b[0] in arr_a:
    print(arr_a.count(arr_b[0]))
    print(arr_a.index(arr_b[0]))