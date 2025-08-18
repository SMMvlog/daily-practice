# Write the program to generate the random password. password size is 10 digit. Password should be combination of alphabets, numbers, and special symbols
import random
import string

def generate_password(length=10):
    # Define character sets
    letters = string.ascii_letters          # a-z, A-Z
    digits = string.digits                  # 0-9
    symbols = string.punctuation            # Special symbols

    # Ensure the password has at least one letter, one digit, and one symbol
    password_chars = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length with a random mix of all character types
#     all_chars = letters + digits + symbols
#     remaining_length = length - len(password_chars)
#     password_chars += random.choices(all_chars, k=remaining_length)

#     # Shuffle the result to avoid predictable patterns
#     random.shuffle(password_chars)

#     # Convert list to string and return
#     return ''.join(password_chars)

# # Generate and print a password
# print("Generated password:", generate_password())

emp_code = []
letters = string.ascii_letters
digits = string.digits
emp_code += random.sample(letters,k=3) 
emp_code += random.sample(digits,k=5)
emp_code = "".join(emp_code) 

print(emp_code)