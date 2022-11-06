import os
import compas
from compas.geometry import Box
from compas.geometry import Transformation
from compas.utilities import linspace

filepath = os.path.join(os.path.dirname(__file__), "session.json")
data = compas.json_load(filepath)

curve = data["curve"]
box = Box(curve.frame_at(curve.domain[0]), 0.8, 0.5, 0.3)

boxes = []
for t in linspace(curve.domain[0], curve.domain[1], 100):
    frame = curve.frame_at(t)
    transformation = Transformation.from_frame_to_frame(box.frame, frame)
    boxes.append(box.transformed(transformation))

data["boxes"] = boxes

compas.json_dump(data, filepath)
