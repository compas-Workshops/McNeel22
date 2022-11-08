import compas
from compas.datastructures import Mesh
from compas.artists import Artist


# Load a mesh from a sample OBJ file
mesh = Mesh.from_obj(compas.get("tubemesh.obj"))


Artist.clear()

# Draw the mesh
artist = Artist(mesh)
artist.draw()
