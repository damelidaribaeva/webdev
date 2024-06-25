def min_of_four(a, b, c, d):
    return min(a, b, c, d)

input_line = input()
a, b, c, d = map(int, input_line.split())

result = min_of_four(a, b, c, d)
print(result)
