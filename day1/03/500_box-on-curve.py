from compas.geometry import Point
from compas.geometry import Polyline
from compas.geometry import NurbsCurve
from compas.geometry import Box
from compas.utilities import linspace
from compas_view2.app import App
from compas_view2.objects import Collection

points = [
    Point(0, 0, 0),
    Point(3, 3, 0),
    Point(6, -6, 3),
    Point(9, 0, 0),
]
curve = NurbsCurve.from_points(points)

frames = []
for t in linspace(curve.domain[0], curve.domain[1], 10):
    frames.append(curve.frame_at(t))

box = Box(frames[0], 0.8, 0.5, 0.3)

viewer = App()
viewer.view.camera.position = [-6, 0, 6]
viewer.view.camera.target = [0, 0, 4]

viewer.add(curve.to_polyline())
viewer.add(Polyline(curve.points), show_points=True)
viewer.add(Collection(frames, [{'size': 0.5} for frame in frames]), linewidth=3)
viewer.add(box)
viewer.show()
