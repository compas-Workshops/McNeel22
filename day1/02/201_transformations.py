from compas.geometry import Box
from compas.geometry import Frame
from compas_view2.app import App


# set up a different coordinate system
frame = Frame([0.5, 0.5, 0.5], [1, 0, 0], [0, 1, 0])

# define a box in the coordinate system
box = Box(frame=frame, xsize=1, ysize=1, zsize=1)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [3, -5, 3]
viewer.view.camera.look_at([0, 0, 0])

viewer.add(box, show_faces=False)
viewer.add(box.frame, linewidth=3)
viewer.show()
