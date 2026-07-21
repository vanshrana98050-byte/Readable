a = int(input())
b = int(input())

x, y = a, b

while y:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)