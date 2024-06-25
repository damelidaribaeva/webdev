x = int(input())

x_str = str(x)

count = 0

for digit in x_str:
    count += int(digit)
print(count)
