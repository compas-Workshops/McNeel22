import os
import compas
from compas.artists import Artist
from compas.colors import Color

# Define a session file
FILE = os.path.join(os.path.dirname(__file__), 'session.json')

# Load the session
session = compas.json_load(FILE)

# Retrieve all the steps
mesh = session['mesh']
dual = session['dual']
frames = session['frames']
model = session['model']

# Clear the scene
Artist.clear()

# Draw the remeshed mesh
artist = Artist(mesh, layer='TubeMesh::Mesh')
artist.draw(disjoint=True, color=Color.red())

# Draw the dual
artist = Artist(dual, layer='TubeMesh::Dual')
artist.draw(disjoint=True, color=Color.green())

# Draw the frames
artist = Artist(frames, layer='TubeMesh::Frames')
artist.draw(disjoint=True, color=Color.blue())

# Draw the model
artist = Artist(model, layer='TubeMesh::Model')
artist.draw(disjoint=True, color=Color.grey())
