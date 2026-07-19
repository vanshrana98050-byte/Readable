num = 153
digits = str(num)
total = sum(int(d) ** len(digits) for d in digits)
print(total == num)  