x = int(input())

x_str = str(x)

reversed_number = ''

for digit in reversed(x_str):
    reversed_number += digit

result = int(reversed_number)

print(result)
