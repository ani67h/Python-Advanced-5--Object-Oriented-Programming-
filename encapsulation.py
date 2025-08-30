# creating a base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

# creating a derived class
class Derived(Base):
    def __init__(self):

        # calling constructor of base class
        Base.__init__(self)
        print("Calling private member of base class : ")
        print(self.__c)

# driver code
obj1 = Base()
print(obj1.a)        