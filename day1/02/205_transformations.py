from compas.geometry import Point
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Translation
from compas_view2.app import App

# create a box in the world coordinate system
box1 = Box(frame=Frame.worldXY(), xsize=1, ysize=1, zsize=1)

# define a new location for the box
location = Point(0.5, 0.5, 0.5)

# compute a translation transformation
vector = location - box1.frame.point
translation = Translation.from_vector(vector)

# generae a transformed copy of the box
box2 = box1.transformed(translation)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [3, -5, 3]
viewer.view.camera.look_at([0, 0, 0])

viewer.add(box1, show_faces=False)
viewer.add(box1.frame, linewidth=3)

viewer.add(box2, show_faces=False)
viewer.add(box2.frame, linewidth=3)

viewer.show()
