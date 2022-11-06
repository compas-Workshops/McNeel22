from compas.geometry import Box
from compas.colors import Color
from compas.artists import Artist

import compas_rhino
from compas_rhino.conversions import RhinoCurve

guid = compas_rhino.select_curve()
curve = RhinoCurve.from_guid(guid).to_compas()

compas_rhino.rs.HideObject(guid)

box = Box(curve.frame_at(curve.domain[0]), 0.8, 0.5, 0.3)

artist = Artist(curve)
artist.draw()

artist = Artist(box)
artist.draw(color=Color.pink())
