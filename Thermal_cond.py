from classes import Boundary, time_, geometry
from calculation import conductivity


left = Boundary()
right = Boundary()
onedimens = geometry()
tim = time_()

left.set_boundary("Left.txt")
right.set_boundary("Right.txt")
onedimens.set_geometry("Geometry.txt")
print(right.table[0][1])
print(onedimens.length)

conductivity("initial_condition.txt", "coef.txt", "output.txt", onedimens, left, right, tim)

