#wap to find area of circle using radis
radius = float(input("Enter radius of circle :"))

# area of circle
area = 3.14*radius*radius
print("Area of circle is :" + str(area))

# circumference of circle
circumference = 2*3.14*radius
print("Circumference of circle is :" + str(circumference))

# semicircle area 
semicircle_area = (2*3.14*radius)/2
print("Area of semicircle is :" + str(semicircle_area))


# sector area
area_of_sector = (3.14*radius*radius)/360
print("Area of sector is :" + str(area_of_sector))