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

points = []
for t in linspace(curve.domain[0], curve.domain[1], 100):
    points.append(curve.point_at(t))

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [-8, 0, 8]
viewer.view.camera.look_at([0, 0, 3])

viewer.add(curve.to_polyline(), linewidth=3)
viewer.add(Polyline(curve.points), show_points=True)
viewer.add(Collection(points))

viewer.show()
