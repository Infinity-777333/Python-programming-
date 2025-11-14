from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circle_area,perimeter as circle_perimeter
from graphics._3D_graphics.cuboid import surface_area  as cuboid_surface_area,volume as cuboid_volume
from graphics._3D_graphics.sphere import surface_area as sphere_surface_area,volume as sphere_volume

print("Enter the length and width of rectangle")
l=int(input("Length:"))
w=int(input("Width:"))
print("\nArea of rectangle:",rect_area(l,w))
print("Perimeter of the rectangle:",rect_perimeter(l,w))

r=int(input("\n\nEnter the radius of the circle:"))
print("\nArea of the circle :",circle_area(r))
print("Perimeter of the circle:",circle_perimeter(r))

print("\n\nEnter the length, width and height of cuboid")
l=int(input("Length:"))
w=int(input("Width:"))
h=int(input("Height:"))
print("\nSurface area of cuboid:",cuboid_surface_area(l,w,h))
print("\nVolume of the cuboid:",cuboid_volume(l,w,h))

print("\n\nEnter the radius of the sphere:")
r=int(input("Radius:"))
print("\nSurface area of sphere:",sphere_surface_area(r))

print("Volume of sphere:",sphere_volume(r))

