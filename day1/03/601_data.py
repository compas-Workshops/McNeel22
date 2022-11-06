import compas
from compas.geometry import Point
from compas.geometry import NurbsCurve
from compas.geometry import Box
from compas.geometry import Frame

points = [
    Point(0, 0, 0),
    Point(3, 3, 0),
    Point(6, -6, 3),
    Point(9, 0, 0),
]
curve = NurbsCurve.from_points(points)

box = Box(Frame.worldXY(), 0.8, 0.5, 0.3)

compas.json_dump({"curve": curve, "box": box}, "session.json")
