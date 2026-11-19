nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Output: 6

max_sum = float("-inf")
current_sum = 0

for num in nums:
  current_sum = max(current_sum+num,num)
  max_sum = max(current_sum,max_sum)
  
  
  
print(max_sum)