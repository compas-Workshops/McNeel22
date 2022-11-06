from math import radians
from compas.geometry import Point
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Translation
from compas.geometry import Rotation

from compas_view2.app import App

box1 = Box(frame=Frame.worldXY(), xsize=3, ysize=2, zsize=1)

location = Point(2, 2, 2)
vector = location - box1.frame.point
translation = Translation.from_vector(vector)
rotation = Rotation.from_axis_and_angle([1, 0, 0], radians(90))

box2 = box1.copy()
box2.transform(translation)
box2.transform(rotation)

viewer = App()
viewer.view.camera.position = [6, -10, 5]
viewer.view.camera.target = [0, 0, 0]

viewer.add(box1, show_faces=False)
viewer.add(box1.frame, linewidth=3)

viewer.add(box2, show_faces=False)
viewer.add(box2.frame, linewidth=3)

viewer.show()
