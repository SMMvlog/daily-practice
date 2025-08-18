# from boto import client

# bucket = "my_bucket"

# s3 = client('s3', bucket=bucket,access_key_id = 'my_access_key',access_secret = 'my_access_secret')
# if s3:
#     s3.response.get("policy")
    

# string='ABCDEFGABEF'

# print(string[:7])


# Input: test_dict = {‘Manjeet’: [1], ‘Akash’: [1, 8, 9]} 
# Output: {‘Manjeet’: [], ‘Akash’: [8, 9]} 
# Input: test_dict = {‘Manjeet’: [2, 2, 2], ‘Akash’: [2, 2, 2]} 
# Output: {‘Manjeet’: [], ‘Akash’: []}



def remove_common_values(input_dict):
    common_values = set.intersection(*map(set, input_dict.values()))
    print('SSSSSSSSSS---',common_values)
    output_dict = {key: [value for value in values if value not in common_values] for key, values in input_dict.items()}

    return output_dict

# Test cases
test_dict1 = {'Manjeet': [1], 'Akash': [1, 8, 9]}
result1 = remove_common_values(test_dict1)
print(result1)

# test_dict2 = {'Manjeet': [2, 2, 2], 'Akash': [2, 2, 2]}
# result2 = remove_common_values(test_dict2)
# print(result2)
























# test_dict = {"Manjeet": [1], "Akash": [1, 8, 9]}

# for values in test_dict.values():
#     print(values)

# def remove_duplicates(input_dict):
#     output_dict = {}

#     for key, values in input_dict.items():
#         unique_values = list(set(values))
#         unique_values.sort()
#         output_dict[key] = unique_values

#     return output_dict

# # Test cases
# test_dict1 = {'Manjeet': [1], 'Akash': [1, 8, 9]}
# result1 = remove_duplicates(test_dict1)
# print(result1)

# test_dict2 = {'Manjeet': [2, 2, 2], 'Akash': [2, 2, 2]}
# result2 = remove_duplicates(test_dict2)
# print(result2)

    
    
    
    
    

# val_lst =[value for value in test_dict.values()]
# for i in range(len(val_lst)):
#      for key, value in test_dict.items(i):
#          if key       
    
     




# string='ABCDEFGABEF'
# lst = []
# sub_stirng =""
# for i in string:
#     if i not in sub_stirng:
#         sub_stirng += i
#     else:
#         lst.append(sub_stirng)
#         sub_stirng = ""
#         sub_stirng += i
# else:
#     lst.append(sub_stirng)
# highest_length = max(lst,key=len)   
# print(f"{highest_length} = {len(highest_length)}")