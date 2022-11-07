import os
import compas
from compas.geometry import Box
from compas_view2.app import App

# =============================================================================
# Import
# =============================================================================

filepath = os.path.join(os.path.dirname(__file__), "session.json")
data = compas.json_load(filepath)

# =============================================================================
# Do
# =============================================================================

curve = data["curve"]
box = Box(curve.frame_at(curve.domain[0]), 0.8, 0.5, 0.3)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.add(curve.to_polyline())
viewer.add(box)
viewer.show()
