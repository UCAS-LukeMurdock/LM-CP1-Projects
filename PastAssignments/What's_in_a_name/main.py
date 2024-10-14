#Luke Murdock What's in a Name

def area(l, w):
    a = l * w
    return a

def volume(b, h, d):
    height = area(b, h)
    v = height * d
    return v

length1 = 5
width1 = 3
rectangle = area(length1, width1)
print(f"The rectangle's size is: {rectangle}")

length2 = 4
width2 = 6
height2 = 2
prism = volume(length2, width2, height2)
print(f"The prism's size is: {prism}")