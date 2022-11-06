from compas.geometry import Box

from compas_view2.app import App

box = Box.from_diagonal(([0, 0, 0], [1, 1, 1]))

viewer = App()
viewer.view.camera.position = [3, -5, 3]
viewer.view.camera.target = [0, 0, 0]

viewer.add(box, show_faces=False)
viewer.add(box.frame, linewidth=3)
viewer.show()