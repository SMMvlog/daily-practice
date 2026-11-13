# # from multiprocessing import Process


# # def task1():
# #   for i in range(10):
# #     print(i)
# # def task2():
# #   for i in range(10):
# #     print(i)

# # p1 = Process(target=task1)
# # p2 = Process(target=task2)
# # if __name__== "__main__":
# #     p1.start()
# #     p2.start()
# # even = 0
# # for i in range(2,100):
# #     for j in range(2,i):
# #         if i%j==0:
# #             break
# #     else:
# #         if not even%2:
# #           print(i)
# #         even +=1

# # input = input("Enter number\n")

# # for i in range(int(input)):
# #     if i%2 == int(input)%2:
# #         print(i)
# def get_bracket():
#   bracket = "([])"
#   stack = []
#   pairs = {
#       ")":"(",
#       "}":"{",
#       "]":"["
#   }

#   for i in bracket:
#     if i not in pairs:
#       stack.append(i)
#     elif i in pairs:
#        if not stack:
#         return False
#        if stack[-1] !=pairs[i]:
#         return False
      
#        stack.pop()
#   if not stack:
#        return True
#   return False 
# print(get_bracket())

# # numbers = [1, 2, 3, 4, 5]

# # # get_even_odd = lambda x:{i:["even","odd"][i%2] for i in x}
# # # print(get_even_odd(numbers))

# # count_even = 0
# # count_odd = 0

# # for i in numbers:
# #   count_even += i%2 == 0
# #   count_odd += i%2
# # print(count_even)
# # print(count_odd)
# # import time
# # print(time.time())

# # raw_json = [ {"id": 1, "name": "Amol@Ugale!!", "city": "Mum#bai$$"},
# #              {"id": 2, "name": "Jo%hn^Doe", "city": "New*York"},
# #               {"id": 3, "name": "An@na 123", "city": "Bang@lore!!!"}]
# # import string
# # # print(string.ascii_letters)

# # def clean_data(lst):
# #     for dct in lst:
# #         name = ""
# #         city = ""
# #         for i in dct.get("name"):
# #             if i in string.ascii_letters:
# #                 name +=i
# #         dct.update({"name":name}) 
# #         for i in dct.get("city"):
# #             if i in string.ascii_letters:
# #                 city +=i
# #         dct.update({"city":city}) 
# #     return lst
# # print(clean_data(raw_json))       

# # l = ('apple', 'mango', ('apple', 'mango', 'banana', ('orange', 'grapes', ('apple', 'grapes'))))

# # from collections import Counter

# # print(Counter(l))

# # test_list = ['How', 'to', 'use', 'recursive', 'method', 'in', 'Python']
# # test_list = ['How', 'to', 'use', 'recursive', 'method', 'in', 'Python']
# # n=3
# # # Output: ['How to use", 'recursive method in', 'Python']

# # result = []
# # count = 0
# # while True:
# #     add_words = " ".join(test_list[count*n:n+(count*n)])
# #     if not add_words:
# #         break
# #     result.append(add_words)
# #     count +=1
# # print(result)


# # Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
 
# # If there are fewer than k characters left, reverse all of them. 
# # If there are less than 2k but greater than or equal to k characters,
# #  then reverse the first k characters and leave the other as original.
 
 
# # Example 1:
 
# # Input: s = "abcdefg", k = 2

# # Output: "bacdfeg"

# # Example 2:
 
# # Input: s = "abcd", k = 2

# # Output: "bacd"

 
# # Constraints:
 
# # 1 <= s.length <= 104

# # s consists of only lowercase English letters.

# # 1 <= k <= 104

# # print("bacdfeg"[:3][::-1])
# def reverse_words(s,k):
#     if len(s)<k:
#         return s[::-1]
#     if len(s) < k*2 and len(s)==k*2:
#       return s[:k][::-1] + s[k:]
#     result = ""
#     for i in range(0,len(s),k):
#        result += s[i:k+i][::-1]
#     return result
# print(reverse_words("abcd",2))

    
# lst = [[1,2,3,4,5]
#        [3,4,5,6,7]
#        []]

# lst = [1,2,3,4,5,6,7,8,9,10,11,12]


# print({i:["Even","Odd"][i%2] for i in lst})

# for i in range(20):
#     print(f'{i}=={["Even","Odd"][i%2]}')

for i in range(-20,0):
    print(i)