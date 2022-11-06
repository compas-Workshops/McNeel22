from compas.geometry import Point
from compas.geometry import NurbsCurve

points = [
    Point(0, 0, 0),
    Point(3, 3, 0),
    Point(6, -6, 3),
    Point(9, 0, 0),
]
curve = NurbsCurve.from_points(points)

print(curve.points)
print(curve.weights)
print(curve.knots)
print(curve.multiplicities)
print(curve.domain)
print(curve.dimension)
print(curve.degree)
print(curve.is_closed)
print(curve.is_periodic)
