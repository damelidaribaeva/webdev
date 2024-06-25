def power(a, n):
    return pow(a, n)

input_line = input()
a, n = map(float, input_line.split())

result = power(a, int(n)) 
print(result)
