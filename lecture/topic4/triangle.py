from lecture.topic4.shape import Shape

class Triangle(Shape):

    def __init__(self):
        self.num_sides = 3

    # overrides abstract method with implementation
    def sides(self):
        return self.num_sides

    def __str__(self):
        return "I am a triangle with " + str(self.sides()) + " sides."

if __name__ == "__main__":
    t = Triangle()
    print("Object __str__ is: " + str(t))
    print("Number of sides is: " + str(t.sides()))
