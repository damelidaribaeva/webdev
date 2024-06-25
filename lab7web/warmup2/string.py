def string_times(str, n):
  result = ""
  for i in range(n):  
    result = result + str 
  return result

#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'