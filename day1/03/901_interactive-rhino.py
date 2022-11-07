import os
import compas
import compas_rhino
from compas_rhino.conversions import RhinoCurve

guid = compas_rhino.select_curve()
curve = RhinoCurve.from_guid(guid).to_compas()

# =============================================================================
# Export
# =============================================================================

data = {"curve": curve}
filepath = os.path.join(os.path.dirname(__file__), "session.json")

compas.json_dump(data, filepath)
