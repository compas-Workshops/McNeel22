import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.colors import Color


# Load a mesh from a sample OBJ file
mesh = Mesh.from_obj(compas.get("tubemesh.obj"))


# Take a random sample of faces
faces = mesh.face_sample(size=17)

# Take a random smaple of vertices
vertices = mesh.vertex_sample(size=23)

# Assign a color to the faces of the sample
face_color = {face: Color.pink() for face in faces}

# Assign a color to the vertices of the sample
vertex_color = {vertex: Color.pink() for vertex in vertices}


Artist.clear()

# Draw the sampled vertices and faces
# and all the edges
artist = Artist(mesh)
artist.draw_faces(faces=faces, color=face_color)
artist.draw_vertices(vertices=vertices, color=vertex_color)
artist.draw_edges()
