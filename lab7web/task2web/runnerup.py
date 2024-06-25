def find_runner_up_score(arr):
    sorted_arr = sorted(set(arr), reverse=True)
    
    return sorted_arr[1]
n = int(input().strip())
arr = list(map(int, input().strip().split()))


print(find_runner_up_score(arr))
