from compas.datastructures import Mesh
from compas.colors import Color
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)

red = (1.0, 0.0, 0.0)
blue = (0.0, 0.0, 1.0)

halfedge_color = {}
for u, v in mesh.edges():
    halfedge_color[u, v] = blue if mesh.halfedge_face(u, v) is None else red
    halfedge_color[v, u] = blue if mesh.halfedge_face(v, u) is None else red

meshartist = plotter.add(
    mesh,
    sizepolicy="absolute",
    facecolor=(1.0, 0.7, 0.7),
)
meshartist.default_vertexcolor = Color.white()
meshartist.default_facecolor = Color(0.9, 0.9, 0.9)
meshartist.default_edgecolor = Color(0, 0, 0)
meshartist.draw()

meshartist.draw_vertexlabels()
meshartist.draw_facelabels()
meshartist.draw_halfedges(color=halfedge_color)

plotter.zoom_extents()
plotter.show()
