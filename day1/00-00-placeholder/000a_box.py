from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Polygon

box = Box(frame=Frame.worldXY(), xsize=1, ysize=1, zsize=1)

print(box)

print(box.frame)
print(box.xsize)
print(box.ysize)
print(box.zsize)

print(box.area)
print(box.volume)
print(box.dimensions)
print(box.edges)
print(box.faces)
print(box.points)

polygons = []
for face in box.faces:
    points = [box.points[index] for index in face]
    polygon = Polygon(points)
    polygons.append(polygon)

for polygon in polygons:
    print(polygon.area)
