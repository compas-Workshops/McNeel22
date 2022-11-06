import os
import compas
from compas.colors import Color
from compas.geometry import Translation
from compas_view2.app import App

# =============================================================================
# Import
# =============================================================================

filepath = os.path.join(os.path.dirname(__file__), "wall.json")

data = compas.json_load(filepath)

params = data['params']
curve = data["basecurve"]
courses = data["courses"]

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [-4, -6, 2]
viewer.view.camera.target = [3, 0, 1]

viewer.add(curve.to_polyline())

for box in courses[0]:
    viewer.add(box, facecolor=Color.blue().lightened(75), linecolor=Color.blue())

for box in courses[1]:
    box.transform(Translation.from_vector([0, 0, params['H']]))
    viewer.add(box, facecolor=Color.red().lightened(75), linecolor=Color.red())

viewer.run()
