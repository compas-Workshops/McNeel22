from math import radians
from compas.geometry import Point
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Translation
from compas.geometry import Rotation
from compas_view2.app import App

# create a box in the WCS
# use different sizes along different axes
box1 = Box(frame=Frame.worldXY(), xsize=3, ysize=2, zsize=1)

# define a new location for the box
location = Point(2, 2, 2)

# compute the translation transformation to the new location
vector = location - box1.frame.point
translation = Translation.from_vector(vector)

# add a rotation
rotation = Rotation.from_axis_and_angle([1, 0, 0], radians(90))

# make a copy of the box
box2 = box1.copy()

# apply the transformations
box2.transform(translation)
box2.transform(rotation)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [6, -10, 5]
viewer.view.camera.look_at([0, 0, 0])

viewer.add(box1, show_faces=False)
viewer.add(box1.frame, linewidth=3)

viewer.add(box2, show_faces=False)
viewer.add(box2.frame, linewidth=3)

viewer.show()
