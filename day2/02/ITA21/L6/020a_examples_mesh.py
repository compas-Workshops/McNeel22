from compas.artists import Artist
from compas.datastructures import Mesh
from compas.colors import Color
from compas.numerical import dr

# ==============================================================================
# Mesh from meshgrid
# ==============================================================================

mesh = Mesh.from_meshgrid(dx=10, nx=10)

# ==============================================================================
# Attributes
# ==============================================================================

# ==============================================================================
# DR
# ==============================================================================

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
