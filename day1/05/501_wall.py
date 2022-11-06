"""
This script must be executed in the Grasshopper Python Editor.

1. Drop a new GHPython editor component
2. Add input parameter `surface` and connect any rhino surface
3. Paste this script inside the editor and run
4. To visualize results, connect `a` out parameter to a `Draw` COMPAS component

"""
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Vector
from compas_rhino.conversions import RhinoSurface

xsize = 0.0615
ysize = 0.02625
zsize = 0.0260

brick = Box.from_diagonal(([0, 0, 0], [xsize, ysize, zsize]))
brick.frame = Frame.worldXY()

surface = RhinoSurface.from_guid(surface).to_compas()

a = []
a.append(brick)
a.append(surface)
