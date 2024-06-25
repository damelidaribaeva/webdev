N = int(input())
power_of_two = 1

while power_of_two <= N:
    if power_of_two == N:
        print("YES")
        break
    power_of_two *= 2
else:
    print("NO")
