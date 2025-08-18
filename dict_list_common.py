data = [

    {"name": "Alice", "age": 30, "hobbies": ["reading", "hiking"]},

    {"name": "Bob", "age": 25, "hobbies": ["gaming", "coding"]},

    {"name": "Charlie", "age": 35, "hobbies": ["cooking", "hiking"]}

]


# Find users who are having common hobbies 

# Please print output as

# Alice, Charlie are having common hobby as hiking.
# print(len(data))
# print(set(data[0].get("hobbies")) & (set(data[2].get("hobbies"))) & (set(data[2].get("hobbies"))))
# result = ""
# for dct in data:
#     for i in range(len(data)-1):
#         print(i)
#         if set(dct.get("hobbies")) & (set(data[i+1].get("hobbies"))):
#             result += f"{data[i].get("name")},{data[i].get("name")} are having common hobby as {list(set(data[i].get("hobbies")) & (set(data[i+1].get("hobbies")))[0])}"
# print(result)
# pre_result = list(set(data[0].get("hobbies")) & (set(data[2].get("hobbies"))) & (set(data[2].get("hobbies"))))
# result = ""

# for hobby in data:
#     if pre_result[0] in hobby.get("hobbies"):
#         result +=f"{hobby.get("name")}"

        
        
        
        
        
        
        
