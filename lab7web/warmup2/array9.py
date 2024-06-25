def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count = count + 1

  return count
#array_count9([1, 9, 9]) → 2