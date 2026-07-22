a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

result = list(set(a) & set(b) & set(c))

print(result)