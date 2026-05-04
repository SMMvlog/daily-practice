nums = [4, 5, 6, 7, 0, 1, 2]

def find_min(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid
    
    return nums[left]

# Example
arr = [4, 5, 6, 7, 0, 1, 2]
print(find_min(arr))  # Output: 0
