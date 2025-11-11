cal_sqr_area=lambda sqr_side:sqr_side**2
cal_rect_area=lambda length,width:length*width
cal_tri_area=lambda base,height:0.5*base*height

sqr=int(input("Enter the side of the square: "))
print("Enter the length and width of the rectangle: ")
length=int(input("Length: "))
width=int(input("Width: "))
print("Enter the base and height of the triangle: ")
base=int(input("Base: "))
height=int(input("Height: "))

print("\nArea of Square:", cal_sqr_area(sqr))
print("Area of Rectangle:", cal_rect_area(length,width))
print("Area of Triangle:", cal_tri_area(base,height))