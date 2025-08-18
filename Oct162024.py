class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # Private attribute

    # Setter for the age
    def set_age(self, age):
        self.__age = age  # Always sets the age to 35
        return self.__age

    # Getter for the age
    def get_age(self):
        self.__age = 32
        return self.__age

# Example usage
p = Person("Alice", 25)

# Trying to set age to 30
print(p.set_age(30))  # Output: 35
print(p.get_age())  # Output: 35
