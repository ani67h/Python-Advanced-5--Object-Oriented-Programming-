len = int(input("Enter the length of the rectangle (in m) : "))
hei = int(input("Enter the height of the rectangle (in m) : "))

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(len, hei)
print("The area of the rectangle is ",newRectangle.rectangle_area(),"m")        