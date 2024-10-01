#Luke Murdock, Area Calculator

def squareFunc(l):
    a = l ** 2
    return a
def rectFunc(b, h):
    a = b * h
    return a
def triFunc(b, h):
    a = (b * h)/2
    return a
def circleFunc(r):
    a = 3.14 * r**2
    return a
def trapFunc(b1, b2, h):
    a = (b1 + b2)/2*h
    return a


choice = int(input("Do you want the area of a square(1), rectangle(2), triangle(3), a circle(4), or a trapezoid(5)?:" ))

if choice < 4:
    base = int(input("What's the base?:"))
    if choice == 1:
        print("The area of this sqaure is", squareFunc(base))

    height = int(input("What's the height?:"))
    if choice == 2:
        print("The area of this rectangle is", rectFunc(base, height))
    else:
        print("The area of this triangle is", triFunc(base, height))

elif choice == 4:
    radius = int(input("What's the radius?:"))
    print("The area of this circle is", circleFunc(radius))
else:
    base1 = int(input("What's the first base?:"))
    base2 = int(input("What's the second base?:"))
    trapHeight = int(input("What's the height?:"))
    print("The area of this trapezoid is", trapFunc(base1, base2, trapHeight))