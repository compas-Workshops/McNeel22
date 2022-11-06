from compas.geometry import Point
from compas.geometry import Polyline
from compas.geometry import NurbsCurve
from compas_view2.app import App

points = [
    Point(0, 0, 0),
    Point(3, 3, 0),
    Point(6, -6, 3),
    Point(9, 0, 0),
]
curve = NurbsCurve.from_points(points)

viewer = App()
viewer.add(curve.to_polyline())
viewer.add(Polyline(curve.points), show_points=True)
viewer.show()
