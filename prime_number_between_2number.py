start = int(input())
end = int(input())

for num in range(start, end + 1):
    if num > 1:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num, end=" ")