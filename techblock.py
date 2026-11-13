# Given an integer array nums, return an array answer such that:
# answer[i] = product of all nums[j] where j != i.

# You must solve it without using division and in O(n) time.

# nums = [1,2,3,4]
# Output: [24,12,8,6]

# Explanation:
# - answer[0] = 2*3*4 = 24
# - answer[1] = 1*3*4 = 12
# - answer[2] = 1*2*4 = 8
# - answer[3] = 1*2*3 = 6

import gc