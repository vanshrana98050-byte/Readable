nums = list(map(int, input().split()))

n = len(nums) + 1

expected = n * (n + 1) // 2
actual = sum(nums)

print(expected - actual)