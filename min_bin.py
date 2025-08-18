# lst = [4, 5, 6, 7, 0, 1, 2]

def find_min(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid element is greater than right element, min is on the right side
        if nums[mid] > nums[right]:
            left = mid + 1
            print("left---",left)
        else:
            right = mid  # min is on the left side (including mid)
    
    return nums[left]

# Examples
print(find_min([4,5,6,7,1,2,3]))   # Output: 1
print(find_min([40,50,60,10,20,30])) # Output: 10
print(find_min([12,14,16,2,4,6,8,10])) # Output: 2


# l = [1,2,3,4,5,6,7,8,9,10]
# target = 8

# def get_target_el(l,t):
#     left = 0
#     right = len(l)-1

#     while left <= right:
#         mid = (left+right)//2
#         print("mid---",mid)
#         if l[mid] == t:
#             return l[mid]
#         if l[mid] < t:
#             left = mid +1
#             print("left-----",left)
#         else:
#             right = mid -1
#     return -1

# print(get_target_el(l,target))
