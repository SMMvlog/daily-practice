import string
import random
cap_l = random.choice(string.ascii_uppercase)
small = random.choice(string.ascii_lowercase)
special = random.choice(string.punctuation)
all_latter = random.choices(string.ascii_letters,k=8)
digits = random.randint(1000,9999)

password = [
      cap_l,
      small,
      special,
      *all_latter,
      str(digits)
]
random.shuffle(password)
print("".join(password))