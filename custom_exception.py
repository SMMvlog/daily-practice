

class MyCustomError(Exception):
    def __init__(self,age):
        self.age = age
        super().__init__(f"age should be grather than 18")

age = 17
if age<18:
    raise MyCustomError(age)

else:
    print("okay")
