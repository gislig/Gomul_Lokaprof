class SquareVector:
    def __init__(self, vectors = []):
        self.vectors = vectors

    def createPoints(self):
        points = []
        for x in range(1,100 + 1):
            for y in range(1,100 + 1):
                vector = [x,y]
                points.append(vector)
        self.vectors = points

    def getAreaLocation(self, x, y):
        is_in_corner = ""
        for i in self.vectors:
            if i[0] <= 50 and i[1] <= 50 and x <= 50 and y <= 50:
                is_in_corner = "upper_left"
            if i[0] >= 51 and i[1] <= 50 and x >= 51 and y <= 50:
                is_in_corner = "upper_right"
            if i[0] <= 50 and i[1] >= 51 and x <= 50 and y >= 51:
                is_in_corner = "lower_left"
            if i[0] >= 51 and i[1] >= 51 and x >= 51 and y >= 51:
                is_in_corner = "lower_right"
        return is_in_corner


def isPointInUpperLeftQuadrant(p, square):
    p = p.strip().split(" ")
    x = int(p[0])
    y = int(p[1])
    if square.getAreaLocation(x,y) == "upper_left":
        print("{} {}".format(x,y))

def main():
    square = SquareVector()
    square.createPoints()

    f = open("Points.txt","r")
    
    for i in f:
        isPointInUpperLeftQuadrant(i, square)

    f.close()

    #print(square)
main()