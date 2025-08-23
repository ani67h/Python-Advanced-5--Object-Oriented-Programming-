# create class
class Employee:

    # intializing
    def __init__(self,name):
        self.name = name
        print('Employee created')

    # calling destructor    
    def __del__(self):
        print("Destructor called")

obj = Employee("Einstein")   
print(obj.name)
print("Program end...")
# elplicitly delete the object
del obj # deleting the onject
print(obj.name) # it will show error as the object is already deleted