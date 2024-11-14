arr = list(map(int, input().split()))

under_max = 0
over_min = 1000

for elem in arr:
    if elem < 500:
        if elem > under_max:
            under_max = elem
    
    else:
        if elem < over_min:
            over_min = elem

print(under_max, over_min)