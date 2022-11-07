import os
import compas
from compas.artists import Artist


FILE = os.path.join(os.path.dirname(__file__), "exchange.json")


# Import data from the exchange file
data = compas.json_load(FILE)
monkey = data["monkey"]


# Clear the Rhino scene
Artist.clear()

# Draw the monkey
artist = Artist(monkey)
artist.draw(disjoint=True)
