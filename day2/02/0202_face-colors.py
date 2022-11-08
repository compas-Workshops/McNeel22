import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.colors import Color


# Load a mesh from a sample OBJ file
mesh = Mesh.from_obj(compas.get("tubemesh.obj"))


# Take a random sample of faces
faces = mesh.face_sample(size=17)

# Assign a color to the sample of faces
face_color = {face: Color.pink() for face in faces}


Artist.clear()

artist = Artist(mesh)
artist.draw_faces(color=face_color)
