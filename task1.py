import abc
class Shape(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def calc_perimeter(self, input):
         """Method documentation"""
         return 
    
class Triangle(Shape):
    def __init__(self, a, b, c): 
        self.a = a
        self.b = b
        self.c = c

def calc_perimeter(self):
    perim = self.a + self.b + self.c
    print("Consider me implemented", perim)
    return perim

# Creating instances
shape = Shape()  # This will throw an error as you can't create an instance of an abstract class directly
triangle = Triangle(3, 4, 5)

# Printing the result of calc_perimeter method
print("Perimeter of the triangle:", triangle.calc_perimeter())
