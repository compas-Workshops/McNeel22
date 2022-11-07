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

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [-8, 0, 8]
viewer.view.camera.look_at([0, 0, 3])

viewer.add(curve.to_polyline(), linewidth=3)
viewer.add(Polyline(curve.points), show_points=True)

viewer.show()
