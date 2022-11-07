from compas.geometry import Box
from compas_view2.app import App


# use a different box constructor
box = Box.from_diagonal(([0, 0, 0], [1, 1, 1]))

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [3, -5, 3]
viewer.view.camera.look_at([0, 0, 0])

viewer.add(box, show_faces=False)
viewer.add(box.frame, linewidth=3)
viewer.show()
