n, q = map(int, input().split())
nums = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

for idx, query in enumerate(queries):
    # 1 a
    if query[0] == 1:
        a = query[1]
        print(nums[a-1])
    
    # 2 b
    elif query[0] == 2:
        b = query[1]
        if b not in nums:
            print(0)
        else:
            for i in range(len(nums)):
                if nums[i] == b:
                    print(i+1)
                    break

    # 3 s e
    else:
        s = query[1]
        e = query[2]
        nums = nums[s-1:e]
        for i in range(len(nums)):
            print(nums[i], end=" ")