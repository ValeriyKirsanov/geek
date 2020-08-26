
x = int(input("insert number__"))
maximum = 0
while x > 0:
    c = x % 10
    if c >= maximum: maximum = c
    x //= 10
print(maximum)
