x = int(input())
d = int(input())

d_str = str(d)
x_str = str(x)

count = 0

for digit in x_str:
    if digit == d_str:
        count += 1
print(count)
