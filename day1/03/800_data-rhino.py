import os
import compas
from compas.geometry import Transformation
from compas.utilities import linspace
from compas.artists import Artist

filepath = os.path.join(os.path.dirname(__file__), "session.json")
data = compas.json_load(filepath)

curve = data["curve"]
box = data["box"]

frames = []
for t in linspace(curve.domain[0], curve.domain[1], 10):
    frames.append(curve.frame_at(t))

boxes = []
for frame in frames:
    transformation = Transformation.from_frame_to_frame(box.frame, frame)
    boxes.append(box.transformed(transformation))

Artist.clear()

artist = Artist(curve)
artist.draw()

for frame in frames:
    artist = Artist(frame, scale=0.5)
    artist.draw()

for box in boxes:
    artist = Artist(box)
    artist.draw()
