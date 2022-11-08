import compas
from compas.datastructures import Mesh
from compas.artists import Artist

# Load the tubemesh from an OBJ
mesh = Mesh.from_obj(compas.get('tubemesh.obj'))

# Convert all quads to triangles
mesh.quads_to_triangles()

# Clear the scene
Artist.clear()

# Draw the mesh faces
artist = Artist(mesh)
artist.draw_faces()
