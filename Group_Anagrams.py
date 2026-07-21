words = input().split()

groups = {}

for word in words:
    key = ''.join(sorted(word))
    groups.setdefault(key, []).append(word)

print(list(groups.values()))