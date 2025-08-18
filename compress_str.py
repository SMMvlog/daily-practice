string = "aabbbbcccaaa"

sub_str = ""
count = 0


for i in range(len(string)):
    if not sub_str and i==0:
        count +=1
        continue
    if string[i] == string[i-1]:
        count +=1
    else:
        sub_str += f"{string[i]}{count}"
        count =1
        
# else:
#     sub_str += f"{string[i]}{count}"
    
print(sub_str)