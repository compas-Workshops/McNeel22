from compas.geometry import Box
from compas.geometry import Frame

box = Box(frame=Frame.worldXY(), xsize=1, ysize=1, zsize=1)

print(box)
