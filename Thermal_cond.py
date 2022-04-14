from classes import Boundary, time_, geometry
from calculation_flat import conductivity_flat
from calculation_cylinder import conductivity_cylinder

left = Boundary()
right = Boundary()
onedimens = geometry()
tim = time_()

shape = input('Enter flat or cylinder: ')
if shape == 'flat':
    left.set_boundary("Left.txt")
    right.set_boundary("Right.txt")
    onedimens.set_length("Geometry.txt")
    conductivity_flat("initial_condition.txt", "coef.txt", "output.txt", onedimens, left, right, tim)

elif shape == 'cylinder':
    left.table = [[None]*2]*1
    left.table[0][0] , left.table[0][1]  = 0 , 100
    right.set_boundary("R2.txt")
    onedimens.set_radius1("radius1.txt")
    onedimens.set_radius2("radius2.txt")
    conductivity_cylinder("initial_condition.txt", "coef.txt", "output.txt", onedimens, left, right, tim)

