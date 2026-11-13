import pandas as pd
import requests


# data = requests.get('https://jsonplaceholder.typicode.com/posts')
# json_data = data.json()

# print(json_data)

# df = pd.read_json('https://jsonplaceholder.typicode.com/posts')
# print(df.to_string())
import json
# for chunk in pd.read_json('https://jsonplaceholder.typicode.com/posts',lines=True,chunksize=2):
#     print(chunk)
    # print("==="*70)
# url = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.get(url,stream=True)
# for line in response.iter_lines():
#     print(json.dump(line))

# for chunk in pd.read_json('emp.json',lines=True,chunksize=1,usecols=["name"]):
#     print(chunk)
#     print("="*70)

import sys

import sys

# lst = [i for i in range(100000)]
# gen = (i for i in range(100000))

# print(type(lst), sys.getsizeof(lst))
# print(type(gen), sys.getsizeof(gen))
# for i in nums:
#     print(i)
# print("second loop")
# for i in nums:
#     print(i)

# print(sys.getsizeof(nums))

# import sys

# nums = [i for i in range(100)]
# for i in nums:
#     print(i)
# print("second loop")
# for i in nums:
#     print(i)

# print(sys.getsizeof(nums))


# def read_data(filename):
#     with open(filename,'r') as f:
#         for line in f:
#             yield json.loads(line)
# gen = read_data("emp.json")
# print(next(gen))

with open("emp.json",'r') as f:
    gen = (json.loads(line) for line in f)
    for l in gen:
        print(l)

