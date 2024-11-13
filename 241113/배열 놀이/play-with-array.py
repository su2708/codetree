n, q = map(int, input().split())
nums = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

for idx, query in enumerate(queries):
    # 1 a
    if query[0] == 1:
        print(nums[query[1]-1])
    
    # 2 b
    elif query[0] == 2:
        if query[1] not in nums:
            print(0)
        else:
            for i in nums:
                if query[1] == i:
                    print(nums.index(i)+1)
                    break

    # 3 s e
    else:
        for i in range(query[1], query[2]+1):
            print(nums[i-1], end=" ")