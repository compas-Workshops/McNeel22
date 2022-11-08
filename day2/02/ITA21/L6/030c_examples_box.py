import compas_rhino
from compas_rhino.geometry import RhinoBox
from compas.artists import Artist
from compas.geometry import Point, Vector
from compas.datastructures import Mesh
from compas.colors import Color
from compas.numerical import dr

# ==============================================================================
# Mesh from Box
# ==============================================================================

guid = compas_rhino.select_object("Select a box.")
box = RhinoBox.from_guid(guid).to_compas()
mesh = Mesh.from_shape(box)
mesh = mesh.subdivide(scheme="quad", k=2)

# ==============================================================================
# Attributes
# ==============================================================================

mesh.update_default_vertex_attributes(is_anchor=False)
mesh.update_default_vertex_attributes(residual=None)
mesh.update_default_vertex_attributes(px=0, py=0, pz=0)

mesh.update_default_edge_attributes(qpre=1.0)

corners = list(mesh.vertices_where(vertex_degree=3))
mesh.vertices_attribute("is_anchor", True, corners)

# ==============================================================================
# DR
# ==============================================================================

xyz = mesh.vertices_attributes(["x", "y", "z"])
edges = list(mesh.edges())
fixed = list(mesh.vertices_where(is_anchor=True))
loads = mesh.vertices_attributes(["px", "py", "pz"])
qpre = mesh.edges_attribute("qpre")

result = dr(xyz, edges, fixed, loads, qpre=qpre, kmax=100)

for vertex in mesh.vertices():
    mesh.vertex_attributes(vertex, ["x", "y", "z"], result[0][vertex])
    mesh.vertex_attribute(vertex, "residual", Vector(*result[-1][vertex]))

# ==============================================================================
# Viz
# ==============================================================================

artist = Artist(mesh, layer="ITA21::L6::FormFinding")

vertexcolor = {vertex: Color.red() for vertex in mesh.vertices_where(is_anchor=True)}

artist.clear_layer()
artist.draw_mesh(disjoint=True)
artist.draw_vertices(color=vertexcolor)
artist.draw_edges()

# this is necessary to avoid that Rhino on Mac freezes up
# when you use the built-in editor to run this script
Artist.redraw()
