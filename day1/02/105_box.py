from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Line

from compas_view2.app import App

box = Box(frame=Frame.worldXY(), xsize=1, ysize=1, zsize=1)

viewer = App()
viewer.view.camera.position = [5, -3, 2]
viewer.view.camera.target = [0, 0, 0]

eye = Point(1, -2, 2)
target = Point(0, 0, 0)

base = eye.copy()
base.z = 0

viewer.add(base)
viewer.add(eye)
viewer.add(target)
viewer.add(Line(base, eye))
viewer.add(Line(eye, target))

viewer.add(box, show_faces=False, linewidth=3)
viewer.show()
