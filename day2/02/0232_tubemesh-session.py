import os
import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.rpc import Proxy

# CGAL is not available in Rhino, but it is available in our environment
# We can reach it from Rhino through a proxy
meshing = Proxy("compas_cgal.meshing")

# Load the tubemesh from an OBJ
mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

# Convert all quads to triangles
mesh.quads_to_triangles()

# Compute the average edge length
L = sum([mesh.edge_length(*edge) for edge in mesh.edges()])

# Define the target length as half the average
L = 0.5 * L / mesh.number_of_edges()

# Remesh using CGAL through the proxy
V, F = meshing.remesh(mesh.to_vertices_and_faces(), target_edge_length=L)

# Construct a new mesh from the result
mesh = Mesh.from_vertices_and_faces(V, F)

# Define a session file
FILE = os.path.join(os.path.dirname(__file__), "session.json")

# Create the session data
session = {"mesh": mesh}

# Dump the session to the file
compas.json_dump(session, FILE)

# Clear the scene
Artist.clear()

# Draw the new mesh
artist = Artist(mesh)
artist.draw(disjoint=True)
