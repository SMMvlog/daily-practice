# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
 
# If there are fewer than k characters left, reverse all of them. 
# If there are less than 2k but greater than or equal to k characters,
#  then reverse the first k characters and leave the other as original.
 
 
# Example 1:
 
# Input: s = "abcdefg", k = 2

# Output: "bacdfeg"

# Example 2:
 
# Input: s = "abcd", k = 2

# Output: "bacd"

 
# Constraints:
 
# 1 <= s.length <= 104

# s consists of only lowercase English letters.

# 1 <= k <= 104


# def reverse_str(s,k):
#     count = 0
#     result = ""
#     for i in s:
#         if count %2==0:
#             k1=s[count*k:k]
#             result +=k1[::-1]
#         count +=1
#         k +=k
#     return result
    
# print(reverse_str("abcdefg",2))


def reverseStr(s: str, k: int) -> str:
    s = list(s)  # convert to list (strings are immutable)

    for i in range(0, len(s), 2 * k):
        print(i)
        # reverse first k characters
        s[i:i+k] = reversed(s[i:i+k])

    return "".join(s)
print(reverseStr("abcdefg", 2))  # Output: "bacdfeg"
print(reverseStr("abcd", 2))     # Output: "bacd"

a = ["abc","ttt2","rrttd","a","gd","wsx"]

print(max())