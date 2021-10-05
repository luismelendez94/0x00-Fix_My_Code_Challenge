#!/usr/bin/python3
""" File that show calculus of a square """


class Square():
    """ Define class Square """

    def __init__(self, width, height):
        """ Initialite variables """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width + self.height) * 2

    def __str__(self):
        """ Print format """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
