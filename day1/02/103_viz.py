from compas.geometry import Box
from compas.geometry import Frame
from compas_view2.app import App


box = Box(frame=Frame.worldXY(), xsize=1, ysize=1, zsize=1)

# =============================================================================
# Viz
# =============================================================================

viewer = App()

# turn off the faces of the box so we can see the frame
viewer.add(box, show_faces=False)
viewer.add(box.frame, linewidth=3)

viewer.show()
