'''Q1 - Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
      Output: 3
      Explanation: The answer is "abc", with the length of 3.
      
Example 2:

Input: s = "bbbbb"
      Output: 1
      Explanation: The answer is "b", with the length of 1.
      
Example 3:

Input: s = "pwwkew"
      Output: 3
      Explanation: The answer is "wke", with the length of 3.
      Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
# s = "pwwkew"
# sub = ""
# lst = []
# for i in s:
#     if i not in sub:
#           sub += i
#     else:
#         lst.append(sub)
#         sub = ""
#         sub += is
# else:
#     lst.append(sub)
# print(lst)
       
# print(list(len(string) for string in lst))

# import string
# input_str = "We promptly judged antique ivory buckles for the next prize"
# new_s = "".join(sorted(set(input_str.replace(" ","").lower())))
# print("sdadas-------",new_s)
# print("sdadas-------",type(new_s))
# all_alphabet = string.ascii_lowercase
# print("letters-------",all_alphabet)
# if all_alphabet == new_s:
#       print("yes")
# else:
#       print("no")
# lst = ["k","l","o","a","t"]
# lst.sort(reverse=True)
# print(lst)


s = "racecar"
revers = s[::-1]
if s == revers:
      print("palindrome")
else:
      print("not palindrome")