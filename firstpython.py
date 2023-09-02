#Dispaly the output
import math
 
def triangle(base, height):
     return base*height/2
 
def circle(radius):
     return math.pi*(radius**2)
    
 def dounut (outside_radius, inside_radius):
     return circle(outside_radius) - circle(inside_radius)

# Test the functions
base = 5
height = 10
print("Area of the triangle:", triangle(base, height))

radius = 7
print("Area of the circle:", circle(radius))

outside_radius = 20
inside_radius = 8
print("Area of the donut:", dounut(outside_radius, inside_radius))
