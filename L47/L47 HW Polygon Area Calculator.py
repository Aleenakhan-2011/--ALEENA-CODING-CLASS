class shape: #parent class
    def __init__(self, w, l, n):
        self.width = w
        self.length = l
        self.name = n

    def printdetails(self):
        print("Shape Name:", self.name)
        print("Width:", self.width)
        print("Length:", self.length)

class rectangle(shape): #child class
    def __init__(self, wi, le):
        shape_name = "Rectangle"
        super().__init__(wi, le, shape_name)

    def area(self):
        return self.width * self.length
    
class square(shape): #child class
    def __init__(self, s):
        shape_name = "Square"
        super().__init__(s, s, shape_name)

        self.side = s   

    def area(self):
        return self.side * self.side
    
#object which calls the constructor
shape = int(input("Choose a shape to calculate area (1-Rectangle, 2-2Square): "))

if shape == 1:
    w = int(input("Enter the width of the rectangle: "))
    l = int(input("Enter the length of the rectangle: "))

    rect = rectangle(w, l)
    rect.printdetails()
    print("Area of Rectangle:", rect.area())

elif shape == 2:
    s = int(input("Enter the side length of the square: "))
    
    sq = square(s)
    sq.printdetails()
    print("Area of Square:", sq.area())