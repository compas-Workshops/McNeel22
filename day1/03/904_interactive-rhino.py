import os
import compas
from compas.artists import Artist

filepath = os.path.join(os.path.dirname(__file__), "session.json")
data = compas.json_load(filepath)

curve = data["curve"]
boxes = data["boxes"]

Artist.clear()

artist = Artist(curve)
artist.draw()

for box in boxes:
    artist = Artist(box)
    artist.draw()
