s = "abcabcbb"

substring = ""
substring_list = []
for letter in s:
    if letter not in substring:
        substring += letter
    else:
      substring_list.append(substring)
      substring = ""
      substring += letter
else:
    substring_list.append(substring) 
maxlen = max(substring_list,key=len)
# print({maxlen:len(maxlen)})

substring = ""
substring_list = [substring for letter in s if substring+=letter letter not in substring else substring]
    