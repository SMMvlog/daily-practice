# a = {"Name":"Mehboob","Age":31,"location":"Mumbai"}
# result = dict(sorted(a.items(),key = lambda item:item[0]))
# result.popitem()
# print(result)


# c = {}
# d = {}
# print(c==d)

# a = "abzo"
# b = "xyzo"

# # print(set(a).difference(b))

# if sorted(a) != sorted(b):
#     pass





import random
from faker import Faker

fake = Faker()

# Number of records
NUM_USERS = 200
NUM_CATEGORIES = 10
NUM_PRODUCTS = 300
NUM_ORDERS = 500

# 1. Users
# Users
# for i in range(NUM_USERS):
#     name = fake.name().replace("'", "")
#     email = fake.unique.email()
#     phone = str(random.randint(6000000000, 9999999999))  # 10-digit number
#     print(f"INSERT INTO users (name, email, phone) VALUES ('{name}', '{email}', '{phone}');")


# 2. Categories
# categories = ["Electronics", "Clothing", "Books", "Home", "Sports", "Toys", "Beauty", "Shoes", "Grocery", "Stationery"]
# for cat in categories:
#     print(f"INSERT INTO categories (category_name) VALUES ('{cat}');")

# 3. Products
# for i in range(NUM_PRODUCTS):
#     pname = fake.word().capitalize() + " " + fake.word().capitalize()
#     price = round(random.uniform(5, 500), 2)
#     stock = random.randint(1, 100)
#     cat_id = random.randint(1, NUM_CATEGORIES)
#     print(f"INSERT INTO products (name, price, stock, category_id) VALUES ('{pname}', {price}, {stock}, {cat_id});")

# # 4. Orders
# for i in range(NUM_ORDERS):
#     user_id = random.randint(1, NUM_USERS)
#     total_amount = round(random.uniform(20, 2000), 2)
#     print(f"INSERT INTO orders (user_id, total_amount) VALUES ({user_id}, {total_amount});")

# # 5. Order Items
for i in range(NUM_ORDERS * 2):  # ~2 items per order
    order_id = random.randint(1, NUM_ORDERS)
    product_id = random.randint(1, NUM_PRODUCTS)
    quantity = random.randint(1, 5)
    price = round(random.uniform(10, 500), 2)
    print(f"INSERT INTO order_items (order_id, product_id, quantity, price) VALUES ({order_id}, {product_id}, {quantity}, {price});")


