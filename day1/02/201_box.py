from compas.geometry import Box
from compas.geometry import Frame

from compas_view2.app import App

frame = Frame([0.5, 0.5, 0.5], [1, 0, 0], [0, 1, 0])
box = Box(frame=frame, xsize=1, ysize=1, zsize=1)

viewer = App()
viewer.view.camera.position = [3, -5, 3]
viewer.view.camera.target = [0, 0, 0]

viewer.add(box, show_faces=False)
viewer.add(box.frame, linewidth=3)
viewer.show()
