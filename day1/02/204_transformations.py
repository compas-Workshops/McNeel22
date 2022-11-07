from compas.geometry import Point
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Translation
from compas_view2.app import App


box = Box(frame=Frame.worldXY(), xsize=1, ysize=1, zsize=1)

location = Point(0.5, 0.5, 0.5)
vector = location - box.frame.point
translation = Translation.from_vector(vector)

box.transform(translation)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [3, -5, 3]
viewer.view.camera.look_at([0, 0, 0])

viewer.add(box, show_faces=False)
viewer.add(box.frame, linewidth=3)
viewer.show()
