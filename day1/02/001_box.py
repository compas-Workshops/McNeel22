from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector

# define a coordinate system
frame = Frame(Point(0, 0, 0), Vector.Xaxis(), Vector.Yaxis())

# create a box in the coordinate system
box = Box(frame=frame, xsize=1, ysize=1, zsize=1)

print(box)
