import os
import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.colors import Color

# Define a session file
FILE = os.path.join(os.path.dirname(__file__), "session.json")

# Load the session
session = compas.json_load(FILE)

# Retrieve the dual mesh from the session
dual = session["dual"]

# Subdivide the dual using the frame scheme
frames = dual.subdivide(scheme="frames", offset=0.1)

# Store the subd mesh in the session
session["frames"] = frames

# Dump the session back to the file
compas.json_dump(session, FILE)

# Clear the scene
Artist.clear()

# Draw the new mesh
artist = Artist(frames)
artist.draw(disjoint=True)
