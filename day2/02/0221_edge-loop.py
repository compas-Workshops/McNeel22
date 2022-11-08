import compas
import compas_rhino
from compas.datastructures import Mesh
from compas.geometry import Line, Plane, Circle
from compas.geometry import Cylinder
from compas.artists import Artist
from compas.colors import Color

Artist.clear()

# Load a mesh from a sample OBJ file
mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

# Draw the mesh so we can select some of its components
artist = Artist(mesh)
guids = artist.draw_edges()  # store the guids of the edges so we can identify them
artist.draw_faces(join_faces=True, color=Color.blue().lightened(50).rgb255)  # the fact that .rgb255 is necessary is a bug
artist.redraw()

# Map the guids to edges
guid_edge = dict(zip(guids, mesh.edges()))

# Container for the pipe GUIDs
pipes = []

while True:

    compas_rhino.rs.UnselectAllObjects()

    # Select an line in Rhino
    guids = compas_rhino.select_lines()

    # Provide an exit for the loop
    if not guids:
        break

    # Make sure to only select one :)
    guid = guids[0]

    # Find the matching edge
    start = guid_edge[guid]

    # Compute the corresponding edge loop
    loop = mesh.edge_loop(start)

    # Give the edges on the loop a color
    edge_color = {}
    for u, v in loop:
        edge_color[u, v] = edge_color[v, u] = Color.pink()

    # Give the start edge a different color
    u, v = start
    edge_color[u, v] = Color.green()
    edge_color[v, u] = Color.green()

    # Clear the previously drawn loop
    if pipes:
        compas_rhino.delete_objects(pipes)
        pipes = []

    # Draw the edges of the loop as pipes so you see them properly
    for u, v in loop:
        ab = Line(mesh.vertex_coordinates(u), mesh.vertex_coordinates(v))
        pipe = Cylinder(Circle(Plane(ab.midpoint, ab.direction), 0.05), ab.length)
        guids = Artist(pipe).draw(color=edge_color[u, v])
        pipes += guids

    Artist.redraw()
