# Anis 58
#
from abc import ABC,abstractmethod  # abstract class er jonno inform kore nite hoy
class Shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod   # dite hbe...na dile o error dibo nah
    def area(self):   # ei method er real body nai...override kore use korbo  # Abstract Class ke inhirit korle = @abstractmethod must must use korte hobe
        pass


class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle : ",area)


class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Triangle : ",area)

# s1 = Shape(10,20)  --->> Abstract Class er kono Object Create kora jabe nah
# s1.area()

t1 = Triangle(20,30)
t1.area()

r1 = Rectangle(20,30)
r1.area()
