def xor(x, y):
    return (x and not y) or (not x and y)

input_line = input()
x, y = map(int, input_line.split())

result = xor(x, y)
print(int(result)) 
