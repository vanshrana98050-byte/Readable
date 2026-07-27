from bisect import bisect_left

nums = list(map(int, input().split()))

lis = []

for num in nums:

    pos = bisect_left(lis, num)

    if pos == len(lis):
        lis.append(num)
    else:
        lis[pos] = num

print(len(lis))