from compas.geometry import Box
from compas.geometry import Frame

box = Box(frame=Frame.worldXY(), xsize=1, ysize=1, zsize=1)

print(box.frame.point)
print(box.frame.xaxis)
print(box.frame.yaxis)
print(box.frame.zaxis)
