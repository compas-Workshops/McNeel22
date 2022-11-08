import compas
from compas.datastructures import Mesh
from compas.artists import Artist


# Load a mesh from a sample OBJ file
mesh = Mesh.from_obj(compas.get("tubemesh.obj"))


Artist.clear()

# Draw the mesh as a collection of vertices and faces
artist = Artist(mesh)
artist.draw_faces()
artist.draw_vertices()
