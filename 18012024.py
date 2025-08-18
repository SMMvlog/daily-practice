def is_palindrome(s):
  return s == s[::-1]

def StringChallenge(strParam):
  if is_palindrome(strParam):
    return "palindrome"
    
  n = len(strParam)
  varFiltersCg = []
    
  for i in range(n):
      temp = strParam[:i] + strParam[i+1:]
      if is_palindrome(temp) and len(temp) >= 3:
          return strParam[i]
    
  for i in range(n):
      for j in range(i+1, n):
          temp = strParam[:i] + strParam[i+1:j] + strParam[j+1:]
          if is_palindrome(temp) and len(temp) >= 3:
              return strParam[i] + strParam[j]
    
  return "not possible"

print(StringChallenge("abjchba"))  # Output: "jc"
print(StringChallenge("racecar"))  # Output: "palindrome"
print(StringChallenge("abcdef"))   # Output: "not possible"
print(StringChallenge("aabbcc")) 