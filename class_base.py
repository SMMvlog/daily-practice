


class Animal:
    count = 0
    def __init__(self,speak,name):
        self.speak = speak
        self.name = name

    def get_speak(self):
        return self.speak
    
    def show_name(self):
        print(self.name)
    

# Lion = Animal("whow whow","lion")

# print(Lion.get_speak())

# print(Animal.count)

# class Tiger(Animal):
#     def __init__(self,speak,walk,food,name):
#         self.walk = walk
#         self.food = food
#         super().__init__(speak,name)
#         self.speak = "==="

#     # def show_name(self):
#     #     return f"Hello {self.name}"

#     def get_food(self):
#         super().show_name()
#         return f"The {self.name} is {self.food}"
    
# t1 = Tiger("tie tie","tabrak tabrak","non-veg","tiger")

# print(t1.get_speak())


# class Parent:
#     def __init__(self,name):
#         self.name = name
#     def greet(self):
#         print(f"Hello from Parent {self.name}")

# class Child(Parent):
#     def greet(self):
#         # super.__init__(name)
#         super().greet()  # Call Parent's greet
#         print("Hello from Child")

# obj = Child("tttt")
# obj.greet()



# from multiprocessing import Process

# def process_task():
#     print("Running in a process")


# if __name__ == "__main__":
#     p = Process(target=process_task)
#     p.start()
#     p.join()


# from threading import Thread

# def thread_task(a):
#     print("Running in a thread")

# t = Thread(target=thread_task, args=(3,))
# t.start()
# # t.join()




# lst = [1,2,3,4,5,6,7,8,9,10]


# result = list(filter(lambda x:x%2==0,lst))
# print(result)

# def get_even(n):
#     if n%2==0:
#         print(n)
# result = list(map(get_even,lst))
# result


# a = lambda x:x if x%2==0 else False
# print(a(10))


s = "ABCBDEEEED"

seen = set()
count = 0

for ch in s:
    count += 1
    if ch in seen:
        break
    seen.add(ch)

print(count)





