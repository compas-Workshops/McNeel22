from compas.geometry import Box
from compas.geometry import Frame
from compas_view2.app import App

# create a pointcloud
# assign a coordinate frame to every point in the cloud
# reposition a transformed copy of the box in each coordinate system
# use random colors for visualisation


box = Box(frame=Frame.worldXY(), xsize=0.3, ysize=0.2, zsize=0.1)

# =============================================================================
# Viz
# =============================================================================

viewer = App()

viewer.add(box)

viewer.show()
