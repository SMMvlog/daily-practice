test_dict = {'Manjeet': [1], 'Akash': [1, 8, 9]} 
# Output: {‘Manjeet’: [], ‘Akash’: [8, 9]} 
# Input: test_dict = {‘Manjeet’: [2, 2, 2], ‘Akash’: [2, 2, 2]} 
# Output: {‘Manjeet’: [], ‘Akash’: []}




# test_dict = {"Manjeet": [1], "Akash": [1, 8, 9]}
# Output: {"Manjeet": [], "Akash": [8, 9]}

# print(test_dict["Manjeet"] - test_dict["Akash"])
# a = [2, 2, 2]

# a.remove(2)
# a.remove(2)
# print(a)

# test_dict = {"Manjeet": [1], "Akash": [1, 8, 9]}
test_dict = {"Manjeet": [2, 2, 3], "Akash": [2, 2, 2]}

common_values = set(test_dict["Manjeet"]).intersection(set(test_dict["Akash"]))
print(common_values)

for key in test_dict:
    test_dict[key] = [i for i in test_dict[key] if i not in common_values]
print(test_dict)



# Find common elements in all values
# common_values = set(test_dict["Manjeet"]).difference(set(test_dict["Akash"]))
# print(common_values)
# # Remove common values from each list
# for key in test_dict:
#     test_dict[key] = [x for x in test_dict[key] if x not in common_values]

# print(test_dict)




