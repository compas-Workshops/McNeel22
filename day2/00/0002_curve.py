import os
import compas
import compas_rhino
from compas_rhino.conversions import RhinoCurve


FILE = os.path.join(os.path.dirname(__file__), "exchange.json")


# Import data from the exchange file
data = compas.json_load(FILE)


# Select a curve in Rhino
guid = compas_rhino.select_curve()

# Convert to a COMPAS curve
curve = RhinoCurve.from_guid(guid).to_compas()


# Add the curve to the exchange data
data["curve"] = curve

# Export the exchange data
compas.json_dump(data, FILE)
