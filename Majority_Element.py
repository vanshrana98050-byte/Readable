nums = list(map(int, input().split()))

for num in nums:
    if nums.count(num) > len(nums) // 2:
        print(num)
        break