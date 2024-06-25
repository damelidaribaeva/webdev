N = int(input())
K = int(input())

apples_per_student = K // N
remainder = K-(apples_per_student*N)
print(remainder)
