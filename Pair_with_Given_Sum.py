nums = list(map(int, input().split()))
target = int(input())

seen = {}

for num in nums:
    if target - num in seen:
        print(target - num, num)
        break
    seen[num] = True
else:
    print("No Pair")