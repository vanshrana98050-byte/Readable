nums = list(map(int, input().split()))

maxxor = 0
mask = 0

for i in range(31, -1, -1):

    mask |= (1 << i)

    prefixes = set()

    for num in nums:
        prefixes.add(num & mask)

    candidate = maxxor | (1 << i)

    for p in prefixes:
        if candidate ^ p in prefixes:
            maxxor = candidate
            break

print(maxxor)