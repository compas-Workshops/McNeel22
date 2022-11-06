import os
import compas
from compas.geometry import Box
from compas.geometry import Transformation
from compas_view2.app import App

filepath = os.path.join(os.path.dirname(__file__), "session.json")
data = compas.json_load(filepath)

curve = data["curve"]
box = Box(curve.frame_at(curve.domain[0]), 0.8, 0.5, 0.3)

viewer = App()
viewer.add(curve.to_polyline())
viewer.add(box)
viewer.show()
