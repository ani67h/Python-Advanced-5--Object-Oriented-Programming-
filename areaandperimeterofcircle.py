rai = int(input("Enter the radius of the circle (in m) in order to know the area and the perimeter : "))

class area_perimeter:

    def __init__(self, radius):
        self.radius = radius

    def area(self, radius):
        self.radius = radius
        cir_area = 3.1416 * radius ** 2
        print("The area of the ",radius," m radius circle is ",cir_area," m²")

    def peri(self, radius):
        self.radius = radius
        cir_peri = 2 * 3.1416 * radius
        print("The perimeter of the ",radius," m radius circle is ",cir_peri," m") 

circle = area_perimeter(rai)
circle.area(rai)        
circle.peri(rai)   