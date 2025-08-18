# 1 - Write a recursive function to calculate the factorial of a given number.

# solution

def get_factorial(n):
    if n==1:
        return 1
    return n * get_factorial(n-1)
# print(get_factorial(5))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # 8
