nums = [5,7,7,8,8,10]
target = 8

def binary_search(lst,target):
    try:
        low = 0
        high = len(lst)-1
        result = [-1,-1]
        while low<=high:
            mid = (low+high)//2
            if lst[mid] == target:
                if result[0] == -1:
                    result[0] = mid
                else:
                    result[1] = mid
                low =mid+1
            else:
                if lst[mid] <target:
                    low =mid+1
                    
                else:
                    high =mid-1
                    
        return result
    except Exception as ex:
        print(ex)
        return False
    
print(binary_search(nums,target))