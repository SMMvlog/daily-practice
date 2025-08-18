class A:
    def show(self):
        print("hello Mehboob")

obj = A()
obj.show()
def new_show():
    print("Hello SHaikh")


class B(A):
    pass

bobj=B()
obj.show = new_show

bobj.show()


