import math

def area_of_rectangle(length, width):
    """
    This function returns the area of a rectangle for a given length and width
    """
    if type(length) != str and type(width) != str:
        return length * width
    else:
        print('All arguments must be numbers')

def area_of_circle(radius):
    """
    This function returns the area of a circle for a given radius
    """
    if type(radius) != str:
        return radius ** 2 * math.pi
    else:
        print('The argument must be a number')