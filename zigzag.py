s = "PAYPALISHIRING"
row = 3
pre_row = row
result = []
i = 0
while i <= len(s)+1:
    print("i--",i)
    r = s[i:row]
    result.append(r)
    i +=pre_row
    print("iii---",i)
    row +=pre_row
    print("row---",row)

# print(result)
import string

print(string.vowels)

