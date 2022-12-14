from compas.geometry import Box
from compas.geometry import Frame
from compas.colors import Color
from compas_view2.app import App


box = Box(frame=Frame.worldXY(), xsize=1, ysize=1, zsize=1)

# =============================================================================
# Viz
# =============================================================================

viewer = App()

viewer.add(
    box,
    facecolor=Color.blue().lightened(50),
    linecolor=Color.blue(),
)

# add the frame of the box to the view
viewer.add(box.frame)

viewer.show()
