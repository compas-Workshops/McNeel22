import compas_rhino
from compas_rhino.geometry import RhinoBox
from compas.artists import Artist
from compas.geometry import Vector
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

compas_rhino.rs.HideObject(guid)

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


def update_equilibrium():
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


def draw():
    artist = Artist(mesh, layer="ITA21::L6::FormFinding")

    vertexcolor = {vertex: Color.red() for vertex in mesh.vertices_where(is_anchor=True)}

    artist.clear_layer()
    artist.draw_mesh(disjoint=True)
    artist.draw_vertices(color=vertexcolor)
    guids = artist.draw_edges()
    edges = list(mesh.edges())

    # this is necessary to avoid that Rhino on Mac freezes up
    # when you use the built-in editor to run this script
    Artist.redraw()

    return dict(zip(guids, edges)), dict(zip(edges, guids))


# ==============================================================================
# Interactive
# ==============================================================================

while True:
    update_equilibrium()
    guid_edge, edge_guid = draw()

    guids = compas_rhino.select_lines("Select edges of the mesh.")
    if not guids:
        break

    guid = guids[0]
    if guid not in guid_edge:
        break

    edge = guid_edge[guid]
    loop = mesh.edge_loop(edge)
    guids = [edge_guid.get((u, v)) if (u, v) in edge_guid else edge_guid.get((v, u)) for u, v in loop]

    compas_rhino.rs.SelectObjects(guids)
    compas_rhino.rs.Redraw()

    q = compas_rhino.rs.GetReal("Force density?", 1.0, 0.1, 100.0)
    if not q:
        break

    mesh.edges_attribute("qpre", q, loop)
    compas_rhino.rs.UnselectObjects(guids)
