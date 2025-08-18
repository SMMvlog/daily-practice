# '''
# Q1 - Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
#       Output: 3
#       Explanation: The answer is "abc", with the length of 3.
      
# Example 2:

# Input: s = "bbbbb"
#       Output: 1
#       Explanation: The answer is "b", with the length of 1.
      
# Example 3:

# Input: s = "pwwkew"
#       Output: 3
#       Explanation: The answer is "wke", with the length of 3.
#       Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.







s = "abcabcbb"
subs = ""
lst = []
index = 0
# last_position = s.rfind(i)
# print(last_position)
# print(len(s))
for i in s:
    index += 1
    last_position = s.rfind(i)
    if i not in subs:
        subs += i
        if index == len(s):
            lst.append(subs)
            break
    else:
        lst.append(subs)
        if index == len(s):
            subs = ""
            subs +=i
            lst.append(subs)
            break
        subs = ""
        subs += i
result = max(lst, key=len)       
print({result: len(result)})