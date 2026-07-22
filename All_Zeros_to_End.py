nums = list(map(int, input().split()))

result = [x for x in nums if x != 0]
result.extend([0] * nums.count(0))

print(result)