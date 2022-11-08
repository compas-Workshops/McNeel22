import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.colors import Color


# Load a mesh from a sample OBJ file
mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

# Take a random vertex
vertex = mesh.vertex_sample(size=1)[0]

# Identify the neighbors of the vertex
nbrs = mesh.vertex_neighbors(vertex)

# Identify the edges connected to the vertex
edges = mesh.vertex_edges(vertex)

# Assign a color to the sample vertex
# and add a label
vertex_color = {vertex: Color.pink()}
vertex_text = {vertex: str(vertex)}

# Assign a color to the neighbour vertices
# and add a label
for nbr in nbrs:
    vertex_color[nbr] = Color.black()
    vertex_text[nbr] = str(nbr)

# Assign a color and label to the connected edges
edge_color = {edge: Color.white() for edge in edges}
edge_text = {edge: str(edge) for edge in edges}


Artist.clear()

artist = Artist(mesh)
artist.draw_vertices(vertices=[vertex] + nbrs, color=vertex_color)
artist.draw_edges(color=edge_color)
artist.draw_vertexlabels(text=vertex_text)
artist.draw_edgelabels(text=edge_text)
