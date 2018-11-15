class Rectangle:
    def __init__(self, Height, Width):
        self.Height = Height
        self.Width = Width

    def area(self):
        return self.Height * self.Width
    
    def circumference(self):
        return 2 * self.Height + 2 * self.Width

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self,other):
        return self.area() < other.area()

    def __gt__(self,other):
        return self.area() > other.area()


    def __str__(self):
        return "Width: {}, Height: {}".format(self.Width, self.Height)

def main():
    r1 = Rectangle(10,20)
    print(r1)
    print(r1.area())
    print(r1.circumference())

    r2 = Rectangle(10,19)
    if r1 == r2:
        print("The two rectangles are equally large")
    else:
        print("The two rectangles are not equal")


    # Sett inn smá viðbót, ekki í prófinu en ...
    if r1 < r2:
        print("r1 ({}) is less than r2 ({})".format(r1.area(),r2.area()))

    if r1 > r2:
        print("r1 ({}) is greater than r2 ({})".format(r1.area(),r2.area()))


main()