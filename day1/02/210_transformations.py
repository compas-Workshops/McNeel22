from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Transformation
from compas_view2.app import App

# create a box in the WCS
# use different sizes along different axes
box1 = Box(frame=Frame.worldXY(), xsize=3, ysize=2, zsize=1)

# define a new coordinate frame
frame = Frame([2, 2, 2], [1, 0, 0], [0, 0, 1])

# compute the transformation from the WCS to the new frame
transformation = Transformation.from_frame_to_frame(box1.frame, frame)

# generate a transformed copy of the box
box2 = box1.transformed(transformation)

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
