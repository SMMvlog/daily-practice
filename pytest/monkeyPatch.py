class Person:
    def greet(self):
        return "Hello!"

# Normal behavior
p = Person()
print(p.greet())  # Output: Hello!

# Monkey patching: changing greet method
def new_greet(self):
    return "Hi there!"

Person.greet = new_greet

print(p.greet())  # Output: Hi there!
