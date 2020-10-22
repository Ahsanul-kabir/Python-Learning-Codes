class Shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        pass   # Pass nothing that means Null

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle : ",area)


class Rectangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Rectangle : ",area)


T = Triangle(20,30)
T.area()
R = Rectangle(20,10)
R.area()