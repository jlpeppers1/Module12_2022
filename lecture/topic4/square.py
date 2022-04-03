from lecture.topic3.shape import Shape

class InvalidSideError(Exception):
    pass

class Square(Shape):

    def __init__(self, len, wid):
        if (len < 0) or (wid < 0):
            raise InvalidSideError
        self.length = len
        self.width = wid
    #    self.num_of_sides = 4

    def area(self):
        return self.length * self.width

    def sides(self):
        return self.num_of_sides

    def __str__(self):
        return "I am a Square with 2 sides.\nLength: " + str(self.length) + "\nWidth: " + str(self.width)

if __name__ == "__main__":
    s = Square(4,10)
    #notice it breaks on above line since there is no sides implemented....
    print("Object __str__ is: " + str(s))
    #print("Number of sides is: " + str(s.sides()))
    print("Area is:" + str(s.area()))
