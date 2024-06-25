def max_end3(nums):
    max_value = max(nums[0], nums[-1])
    return [max_value, max_value, max_value]

#max_end3([11, 5, 9]) → [11, 11, 11]