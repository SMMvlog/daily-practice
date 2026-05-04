nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]

def ArrayChallenge(arr):
    n = len(arr)
    dp = [1] * n  # every element is at least length 1

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(ArrayChallenge(nums))














# pre_result = []
# result = []
# n =len(nums)
# count = 0

# while count < n:
#     for i in nums:
#         if not pre_result[count:]:
#             pre_result.append(i)
#         elif pre_result[-1] <i:
#             pre_result.append(i)
#     print(pre_result)
#     if len(result) < len(pre_result) and sum(result) < sum(pre_result):
#         result.append(pre_result)
#     pre_result = []
#     count +=1
# print(result) 


