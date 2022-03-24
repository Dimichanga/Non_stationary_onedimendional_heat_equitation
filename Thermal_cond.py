from classes import Boundary, time_, geometry
from calculation_flat import conductivity_flat


left = Boundary()
right = Boundary()
onedimens = geometry()
tim = time_()

left.set_boundary("Left.txt")
right.set_boundary("Right.txt")
onedimens.set_length("Geometry.txt")

conductivity_flat("initial_condition.txt", "coef.txt", "output.txt", onedimens, left, right, tim)

