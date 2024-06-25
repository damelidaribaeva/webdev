def centered_average(nums):
    min_val = min(nums)
    max_val = max(nums)
    
    sum_nums = sum(nums)

    sum_without_min_max = sum_nums - min_val - max_val
    
    count_without_min_max = len(nums) - 2
    
    centered_avg = sum_without_min_max // count_without_min_max
    
    return centered_avg