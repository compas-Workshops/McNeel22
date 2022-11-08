import os
import compas
from compas.datastructures import Mesh
from compas.artists import Artist

# Define a session file
FILE = os.path.join(os.path.dirname(__file__), "session.json")

# Load the session
session = compas.json_load(FILE)

# Retrieve the remeshed mesh from the session
mesh = session['mesh']

# Compute the dual
dual = mesh.dual()

# Store the dual in the session
session['dual'] = dual

# Dump the session back to the file
compas.json_dump(session, FILE)

# Clear the scene
Artist.clear()

# Draw the new mesh
artist = Artist(dual)
artist.draw(disjoint=True)
