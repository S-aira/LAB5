import math
class Shape:
    def __iniit__(self):
         pass
    def area(self):
        pass
    def perimeter(self):
        pass
     def area_to_perimeter_ratio(self):
        pass

class Rectangle(Shape):
    def _init_(self, length, width):
        super()._init_()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        self.__length = length
    
    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        self.__width = width

     def area_to_perimeter_ratio(self):
        return self.area() / self.perimeter()

class Circle(Shape):
    def _init_(self, radius):
        super()._init_()
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius

    def area_to_perimeter_ratio(self):
        return self.area() / self.perimeter()

if __name__ == "__main__":
   
    shape= Shape()
    print("Area:", shape.area())
     print("Perimeter:", shape.perimeter())
    # Test the Rectangle and Circle classes
    rectangle = Rectangle(4, 5)
    print("Rectangle Area:", rectangle.area())
    print("Rectangle Perimeter:", rectangle.perimeter())
     print("Rectangle Length:", rectangle.get_length())
    print("Rectangle Width:", rectangle.get_width())
    rectangle.set_length(6)
    rectangle.set_width(7)
    print("Updated Rectangle Area:", rectangle.area())
    print("Updated Rectangle Perimeter:", rectangle.perimeter())

    circle = Circle(3)
    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())  
    print("Circle Radius:", circle.get_radius())
    circle.set_radius(4)
    print("Updated Circle Area:", circle.area())
    print("Updated Circle Perimeter:", circle.perimeter()) 

