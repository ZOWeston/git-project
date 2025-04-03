height = int(input("Enter the height of the the object as a integer: "))
length = int(input("Enter the length of the the object as a integer: "))    #without using classes or OOP, I found it better and more convenient to
width = int(input("Enter the width of the the object as a integer: "))      #define the variables outside of parameters

#Function 1
# Returns Area of Rectangle

def rect_area():
    area = length * width
    return area

#Function 2
# Returns Surface Area of Rectangular Solid

def rect_surface_area():
    surface_area = 2*length*width + 2*length*height + 2*width*height    #here I used the formula I found online for rectangle surface area
    return surface_area                                                 #2lw + 2lh + 2wh
# Request the dimension of a solid rectangular object                   #I have no idea if its right, im not a math wiz :P


print("Length = " + str(length) + " Width = " + str(width) + " Height = " + str(height))
print("Total Surface Area = " + str(rect_surface_area()))
print("Area of the rectangle: " + str(rect_area()))

