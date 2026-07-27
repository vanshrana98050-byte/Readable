n = int(input())

intervals = []

for _ in range(n):
    intervals.append(list(map(int, input().split())))

intervals.sort()

merged = [intervals[0]]

for current in intervals[1:]:
    last = merged[-1]

    if current[0] <= last[1]:
        last[1] = max(last[1], current[1])
    else:
        merged.append(current)

print(merged)