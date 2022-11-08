import os
import compas
from compas.datastructures import Mesh
from compas.datastructures import mesh_thicken
from compas.artists import Artist
from compas.colors import Color

# Define a session file
FILE = os.path.join(os.path.dirname(__file__), "session.json")

# Load the session
session = compas.json_load(FILE)

# Retrieve the subd mesh from the session
frames = session["frames"]

# Add thickness
model = mesh_thicken(frames, thickness=0.05)

# Store the thickened model in the session
session["model"] = model

# Dump the session back to the file
compas.json_dump(session, FILE)

# Clear the scene
Artist.clear()

# Draw the new mesh
artist = Artist(model)
artist.draw(disjoint=True)
