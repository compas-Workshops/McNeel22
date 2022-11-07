"""
This script must be executed in the Grasshopper Python Editor.

1. Drop a new GHPython editor component
2. Paste this script inside the editor and run
3. To visualize results, connect `a` out parameter to a `Draw` COMPAS component

"""
from compas.geometry import Box
from compas.geometry import Frame

xsize = 0.15
ysize = 0.08
zsize = 0.07

brick = Box.from_diagonal(([0, 0, 0], [xsize, ysize, zsize]))
brick.frame = Frame.worldXY()

a = []
a.append(brick)
