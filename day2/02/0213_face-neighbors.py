import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.colors import Color


# Load a mesh from a sample OBJ file
mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

# Take a random face
face = mesh.face_sample(size=1)[0]

# Identify the neighbors of the face
nbrs = mesh.face_neighbors(face)

# Assign a color to the sample face
# and add a label
face_color = {face: Color.pink()}
face_text = {face: str(face)}

# Assign a color to the neighbour faces
# and add a label
for nbr in nbrs:
    face_color[nbr] = Color.blue()
    face_text[nbr] = str(nbr)


Artist.clear()

artist = Artist(mesh)
artist.draw_faces(color=face_color)
artist.draw_edges()
artist.draw_facelabels(text=face_text)
