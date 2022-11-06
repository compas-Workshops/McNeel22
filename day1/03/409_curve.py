from compas.geometry import Point
from compas.geometry import Polyline
from compas.geometry import NurbsCurve
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

viewer = App()
viewer.view.camera.position = [-6, 0, 6]
viewer.view.camera.target = [0, 0, 4]

viewer.add(curve.to_polyline())
viewer.add(Polyline(curve.points), show_points=True)
viewer.add(Collection(frames), linewidth=3)
viewer.show()
