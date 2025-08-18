# l = [1, 0, 1, 0, 1, 0, 1, 0]

# count_1 = sum(x * 1 for x in l)  # Adding all 1s (0s don't contribute)
# count_0 = len(l) - count_1  # Since total elements - count of 1s = count of 0s

# print("Count of 1:", count_1)
# # print("Count of 0:", count_0)


s = "Hello, world! How are you?"
# count = 1  # Start with 1 because the last word won't have a space after it

# for char in s:
#     count += char == ' '  # This will add 1 if the character is a space

# print(count)


l = [1, 2, 3, 4, 5, 6, 7, 8]

# even_numbers = [x * (x % 2 == 0) for x in l]  # Multiplying by (x % 2 == 0) keeps evens and makes odds zero
# # even_numbers = list(set(even_numbers) - {0})  # Removing zeros

# print(sum(i * (i%2==0) for i in l))

# char_count = 0
# for i in s:
#     char_count += (i!=" ")
# print(char_count)
# print(len(s))


# print(result)

# l = [1, 0, 1, 0, 1, 0, 1, 0]

# count_one = 0
# count_zero = 0
# for num in l:
#     count_zero += (num==0)
#     count_one += (num==1)
# print(f"count_one: {count_one}")
# print(f"count_zero: {count_zero}")

# n = 37
# result = ["even","odd"][n%2]
print(37%2)