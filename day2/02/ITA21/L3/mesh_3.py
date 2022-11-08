from compas.datastructures import Mesh
from compas.colors import Color
from compas_plotters import Plotter

plotter = Plotter(figsize=(8, 8))

mesh = Mesh.from_meshgrid(dx=2, nx=2)
VERTEX = 4

vertex_color = {VERTEX: (1.0, 0.0, 0.0)}
for nbr in mesh.vertex_neighbors(VERTEX):
    vertex_color[nbr] = (1.0, 0.9, 0.9)

halfedges = []
for u, v in mesh.vertex_edges(VERTEX):
    halfedges.append((u, v))
    halfedges.append((v, u))

meshartist = plotter.add(mesh, vertexcolor=vertex_color, sizepolicy="absolute")
meshartist.default_vertexcolor = Color.white()
meshartist.default_facecolor = Color(0.9, 0.9, 0.9)
meshartist.default_edgecolor = Color(0, 0, 0)
meshartist.draw()

meshartist.draw_vertexlabels()
meshartist.draw_facelabels()

meshartist.draw_halfedges(halfedges=halfedges, color=(1, 0, 0))

plotter.zoom_extents()
plotter.show()
