list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

if sorted(list1) == sorted(list2):
    print("Equal")
else:
    print("Not Equal")