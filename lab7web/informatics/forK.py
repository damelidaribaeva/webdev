def calculate_sum_of_numbers(N):
    sum_numbers = 0
    
    for _ in range(N):
        number = int(input().strip())
        sum_numbers += number 
    
    return sum_numbers

N = int(input().strip())

result = calculate_sum_of_numbers(N)

print(result)
