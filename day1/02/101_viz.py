from compas.geometry import Box
from compas.geometry import Frame
from compas.colors import Color
from compas_view2.app import App


box = Box(frame=Frame.worldXY(), xsize=1, ysize=1, zsize=1)

# =============================================================================
# Viz
# =============================================================================

viewer = App()

# color the faces of the box in light blue
# and the edges in dark(er) blue
viewer.add(
    box,
    facecolor=Color.blue().lightened(50),
    linecolor=Color.blue(),
)

viewer.show()
